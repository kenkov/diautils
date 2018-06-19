#! /usr/bin/env python
# coding:utf-8


"""JSON 形式対話データ

    [{"text": "発話1", ...}, {"text": "発話2", ...}, {"text": "発話3", ...}, ...]


をタブ区切り形式対話データ

    発話1<TAB>発話2<TAB>発話3<TAB>...

に変換するスクリプト
"""

import json


def convert_jsond2tabd(json_str):
    texts = [item["text"]
             for item in json.loads(json_str)]
    return "\t".join(texts)


if __name__ == '__main__':
    import sys

    for line in sys.stdin:
        line = line.strip("\n")
        tabd = convert_jsond2tabd(line)
        print(tabd)
