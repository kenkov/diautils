#! /usr/bin/env python
# coding: utf-8


"""tabd形式の対話データを paird 形式の対話データ

    発話1<TAB>発話2
    発話2<TAB>発話3
    発話3<TAB>発話4
    ...

に変換するスクリプト
"""


def convert_tabd2paird(tabd):
    replies = tabd.split("\t")
    items = []
    for src, tgt in zip(replies, replies[1:]):
        items.append("{}\t{}".format(src, tgt))
    return items


if __name__ == '__main__':
    import sys

    for line in sys.stdin:
        line = line.strip("\n")
        for item in convert_tabd2paird(line):
            print(item)