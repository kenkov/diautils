#! /usr/bin/env python
# coding:utf-8


"""Twitter のツイートデータから対話データを抽出するスクリプト"""


import json
from collections import defaultdict


ID = "id_str"
REPLY_ID = "in_reply_to_status_id_str"


class TwitterExtractor:
    """ツイートデータから対話データを抽出するクラス"""
    def extract_from_file(self, filename):
        tweets = self._load(filename)
        return self.extract(tweets)

    def extract(self, tweets):
        reply_dic = defaultdict(list)

        for tweet in reversed(tweets):
            if ID not in tweet:
                continue
            if tweet[ID] in reply_dic:
                id_ = tweet[ID]
                if not self._has_reply(tweet):
                    for item in [[tweet] + reply for reply in reply_dic[id_]]:
                        yield item
                    del reply_dic[id_]
                    continue
                reply_id = tweet[REPLY_ID]
                updated_replies = [[tweet] + reply for reply in reply_dic[id_]]
                if reply_id in reply_dic:
                    reply_dic[reply_id] += updated_replies
                else:
                    reply_dic[reply_id] = updated_replies
                del reply_dic[id_]
            else:
                if not self._has_reply(tweet):
                    yield [tweet]
                    continue
                reply_id = tweet[REPLY_ID]
                reply_dic[reply_id].append([tweet])

    def _has_reply(self, tweet):
        return bool(REPLY_ID in tweet and tweet[REPLY_ID] is not None)

    def _load(self, filename):
        tweets = []
        with open(filename) as f:
            for tweet_str in f:
                tweet = json.loads(tweet_str)
                tweets.append(tweet)
        return tweets
