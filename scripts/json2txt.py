#! /usr/bin/env python
# coding:utf-8


"""JSON 対話データ

    [{"text": "発話1", ...}, {"text": "発話2", ...}, {"text": "発話3", ...}, ...]


をテキスト対話データ

    発話1<TAB>発話2<TAB>発話3<TAB>...

に変換するスクリプト。
"""


if __name__ == '__main__':
    import sys
    import json

    for line in sys.stdin:
        replies = [tweet["text"].replace("\n", " ")
                   for tweet in json.loads(line)]
        print("\t".join(replies))
