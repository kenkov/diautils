#! /usr/bin/env python
# coding:utf-8


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
    from diautils.extractor.twitter import TwitterExtractor

    dialog_extractor = TwitterExtractor()

    filename = sys.argv[1]
    for replies in dialog_extractor.extract_from_file(filename):
        replies = [tweet["text"] for tweet in replies]
        for src, tgt in zip(replies, replies[1:]):
            src = preprocess(src)
            tgt = preprocess(tgt)
            if src and tgt:
                print(f"{src}\t{tgt}")
