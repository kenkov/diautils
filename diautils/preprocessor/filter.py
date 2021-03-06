#! /usr/bin/env python
# coding:utf-8


import re
import sys
import diautils.preprocessor.regex as regex_


def _regex_filter(regex, text):
    return bool(regex.search(text))


def len30(text):
    """30文字より大きい長さの文の場合 True を返す"""
    return len(text) > 30


def url(text):
    """URLを含む場合 True を返す"""
    return _regex_filter(regex_.url, text)


def retweet(text):
    """Retweet の場合 True を返す"""
    return _regex_filter(regex_.retweet, text)


def mention(text):
    """Mention の場合 True を返す"""
    return _regex_filter(regex_.mention, text)


def mention_in_sent(text):
    """Mention の場合 True を返す"""
    return _regex_filter(regex_.mention_in_sent, text)


def punc_in_sent(text):
    """句点が文中に存在する場合は True を返す"""
    regex = re.compile(r'.*。.+')
    return _regex_filter(regex, text)


def time(text):
    """時間表現を含む文の場合は True を返す"""
    regex = re.compile(r'今日|明日|明後日|昨日|一昨日|今週|来週|来週|先週|今年|昨年|一昨年|来年')
    return _regex_filter(regex, text)


def demon(text):
    """指示表現を含む文の場合は True を返す"""
    regex = re.compile(r'([こそあど][れの]|ここ|そこ|あそこ|どこ)')
    return _regex_filter(regex, text)


def person(text):
    """人称表現を含む文の場合は True を返す"""
    regex = re.compile(r'くん|君|さん|ちゃん|たん')
    return _regex_filter(regex, text)


def ng(text):
    """NG 語を含む文の場合は True を返す"""
    regex = re.compile(r'(死)')
    return _regex_filter(regex, text)


def empty(text):
    """空白を含む行は True を返す"""
    regex = re.compile(r'^\s*$')
    return _regex_filter(regex, text)


def executor(stream, filter_str, column=None, separator="\t"):
    """エントリポイント

    Args:
        stream: フィルターする文字列を含むストリーム
        filter_str (str): フィルターに使用する関数名。複数指定する場合は「,」で区切る
            例: end_special_char,url
        column (int): 変換対象のカラム番号。カラム番号は 1 からはじまる
        separator (str): column を区切るセパレータ
    """
    if column:
        if type(column) == int:
            column_idxes = [column]
        else:
            column_idxes = column
    if type(filter_str) == str:
        filter_str = [filter_str]
    filters = [eval(code) for code in filter_str]
    for line in stream:
        text = line.strip("\n")
        if column:
            texts = text.split(separator)
            res = []
            for i, text_one in enumerate(texts):
                if i in column_idxes:
                    res.append(text_one)
        else:
            res = [text]
        filter_flag = False
        for text_one in res:
            if any(filter_(text_one) for filter_ in filters):
                filter_flag = True
                break
        if filter_flag:
            continue
        else:
            yield text


def commandline_executor(filter_str, column=0, separator="\t"):
    """python-fire のエントリポイント

    Args:
        filter_str: フィルターに使用する関数名。複数指定する場合は「,」で区切る
            例: end_special_char,url
        column: 変換対象のカラム番号。絡む番号は 1 からはじまる
        separator: column を区切るセパレータ
    """
    return executor(sys.stdin,
                    filter_str,
                    column=column,
                    separator=separator)


if __name__ == "__main__":
    import fire

    fire.Fire(commandline_executor)