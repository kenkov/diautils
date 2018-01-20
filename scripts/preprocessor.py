#! /usr/bin/env python
# coding:utf-8


"""テキスト対話データに前処理を行うスクリプト"""


from diautils.preprocessor.twitter import Preprocessor
from diautils.preprocessor.twitter import TwitterPreprocessor

preprocessor = Preprocessor()
twpreprocessor = TwitterPreprocessor()


def preprocess(text):
    funcs = [preprocessor.remove_link,
             preprocessor.remove_newline,
             twpreprocessor.remove_mention,
             twpreprocessor.remove_retweet,
             twpreprocessor.remove_tag,
             preprocessor.shrink_cont_spaces,
             preprocessor.strip,
             ]
    for func in funcs:
        text = func(text)
    return text


if __name__ == '__main__':
    import sys

    for line in sys.stdin:
        texts = line.strip("\n").split("\t")
        ret = "\t".join(preprocess(text) for text in texts)
        print(ret)
