#! /usr/bin/env python
# coding: utf-8


import re
import sys


def end_special_char(text):
    """文末の特殊文字を削除する"""
    special_chars = ["！"]
    text_ = re.sub(r'({})+$'.format("|".join(special_chars)),
                   '', text)
    return text_


def executor(transformer_str, column=0, separator="\t"):
    """python-fire のエントリポイント

    Args:
        transformer_str: 変換に使用する関数名。複数指定する場合は「,」で区切る
            例: end_special_char,url
        column: 変換対象のカラム番号。絡む番号は 1 からはじまる
        separator: column を区切るセパレータ
    """
    column_idx = column - 1
    transformers = [end_special_char]
    for line in sys.stdin:
        text = line.strip("\n")
        if column:
            texts = text.split(separator)
            text = texts[column_idx]
        for transformer in transformers:
            text = transformer(text)
        if column:
            texts[column_idx] = text
            text = separator.join(texts)
        print(text)

if __name__ == "__main__":
    import fire

    fire.Fire(executor)