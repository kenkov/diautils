#! /usr/bin/env python
# coding: utf-8


"""テキスト対話データ

    発話1<TAB>発話2<TAB>発話3<TAB>...

を、STCテキスト対話データ

    発話1<TAB>発話2
    発話2<TAB>発話3
    発話3<TAB>...

に変換するスクリプト
"""


if __name__ == '__main__':
    import sys

    for line in sys.stdin:
        replies = line.strip("\n").split("\t")
        for src, tgt in zip(replies, replies[1:]):
            print(f"{src}\t{tgt}")
