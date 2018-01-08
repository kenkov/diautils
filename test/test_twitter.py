#! /usr/bin/env python
# coding:utf-8


import unittest
from diautils.extractor.twitter import TwitterExtractor


class TestTwitterExtractor(unittest.TestCase):
    def test_extract(self):
        extractor = TwitterExtractor()
        tweets = [
            {"id_str": 0,
             "text": "おはよう"},
            {"id_str": 1,
             "text": "おはようございます！",
             "in_reply_to_status_id_str": 0},
            {"id_str": 2,
             "text": "おはあり！",
             "in_reply_to_status_id_str": 1},
            {"id_str": 3,
             "text": "疲れた"}
        ]
        res = list(extractor.extract(tweets))
        ans = [[tweets[0], tweets[1], tweets[2]], [tweets[3]]]
        self.assertEqual(self._sorted(res),
                         self._sorted(ans))

    def _sorted(self, replies):
        return list(sorted(replies,
                    key=lambda x: x[0]["id_str"]))
