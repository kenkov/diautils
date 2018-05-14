#! /usr/bin/env python
# coding: utf-8


import re
import sys
import mojimoji
import emoji as emoji_
import diautils.preprocessor.regex as regex_


def emoji2str(text):
    """絵文字を文字列に変換する"""
    return emoji_.demojize(text)


def remove_emoji(text):
    """絵文字を削除する"""
    return "".join(c for c in text if c not in emoji_.UNICODE_EMOJI)


def remove_symbol(text):
    """顔文字等の特殊文字を削除する"""
    # 括弧で囲まれた箇所を消す
    text_ = re.sub(r'([ｍｏｂ]+)?[\(（【][^\(\)（）]*[\)）】]([ｍｏｂ]+)?', '', text)

    # 特殊文字を消す
    regex = re.compile(r'[＼ヾヽ٩\(（【^\(\)（）\)）】／ノﾉ۶＿ゞ＾´ω｀＝ᐛو・ω・｀＊˘￣▽△↑↓←→♪♡；∇꒳°ロ°∀ ＞＜ｏ☆〃□ 🏻ˊᗜˋ●○๑」∠«‘»◜◝（＾＾）╹◡╹⁰▿⁰−≧≦﹃º]')
    text_ = text
    while regex.search(text_):
        text_ = regex.sub("", text_) 

    # 笑表現を削除
    text_ = re.sub(r"[wｗ笑]+", "", text_)

    return text_


def remove_space(text):
    """スペースを削除する"""
    return re.sub(r"\s+", "", text)


def zen(text):
    """半角を全角にする"""
    return mojimoji.han_to_zen(text)


def normalize_punc(text):
    """句読点を正規化する

    正規化は次を行う
    - 「。」の代替となる文字は「。」に変換
    - 文末の「。」は削除する
    - 連続する「、」を一つにする
    - 連続する「。、」を「。」に置き換える
    - 連続する「？」を含む句読点を「？」に置き換える
    """
    text_ = text

    # 「。」の代替となる文字は「。」に変換する
    # ただし、文末の「。」は削除する
    special_chars = r"[！ー－。…．・／〜～]"
    special_chars_regex = re.compile(r'{}{}+'.format(special_chars,
                                                     special_chars))
    while special_chars_regex.search(text_):
        text_ = special_chars_regex.sub("。", text_)
    text_ = re.sub(special_chars, "。", text_)
    text_ = re.sub(r'{}$'.format(special_chars), "", text_)

    # 連続する「、」を一つにする
    # 文末の「、」は削除
    text_ = re.sub(r'、+', '、', text_)
    text_ = re.sub(r'、$', "", text_)

    # 連続する「。、」を「。」におきかえる
    text_ = re.sub(r'[。、]+', '。', text_)

    # 連続する「？」を含む句読点を「？」におきかえる
    text_ = re.sub(r'[？。、]*？[？。、]*', '？', text_)

    return text_


def remove_url(text):
    return regex_.url.sub("", text)


def remove_mention(text):
    return regex_.mention.sub("", text)


def remove_head_mention(text):
    return regex_.head_mention.sub("", text)


def remove_tag(text):
    return regex_.tag.sub("", text)


def executor(stream, transformer_str, column=0, separator="\t",
             debug=False):
    """エントリポイント

    Args:
        stream: 変換する文字列を含むストリーム
        transformer_str (str or tuple): 変換に使用する関数名。複数指定する場合はタプルで指定する
            例: "url"
            例: ("end_special_char", "url")
        column (int): 変換対象のカラム番号。絡む番号は 1 からはじまる
        separator (str): column を区切るセパレータ
    """
    column_idx = column - 1
    if type(transformer_str) == str:
        transformer_str = [transformer_str]
    transformers = [eval(code) for code in transformer_str]
    for line in stream:
        text = line.strip("\n")
        orig_text = text
        if column:
            texts = text.split(separator)
            text = texts[column_idx]
        for transformer in transformers:
            text = transformer(text)
        if column:
            texts[column_idx] = text
            text = separator.join(texts)
        if debug:
            print("DEBUG: from: {}".format(orig_text))
            print("DEBUG: to  : {}".format(text))
        yield text


class Transformer:
    def __init__(self, transformer_str,
                 column=0, separator="\t",
                 debug=False):
        self.transformer_str = transformer_str
        self.column = column
        self.separator = separator

    def transform(self, texts):
        """
        Args:
            texts (List[str]): 変換するテキストのリスト
        """
        return executor(texts, self.transformer_str,
                        column=self.column,
                        separator=self.separator,
                        debug=False)


def commandline_executor(transformer_str, column=0, separator="\t",
                         debug=False):
    """python-fire のエントリポイント

    Args:
        transformer_str: 変換に使用する関数名。複数指定する場合は「,」で区切る
            例: end_special_char,url
        column: 変換対象のカラム番号。絡む番号は 1 からはじまる
        separator: column を区切るセパレータ
    """
    return executor(sys.stdin,
                    transformer_str,
                    column=column,
                    separator=separator,
                    debug=debug)


if __name__ == "__main__":
    import fire

    fire.Fire(commandline_executor)
