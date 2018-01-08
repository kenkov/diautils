#! /usr/bin/env python
# coding:utf-8


if __name__ == '__main__':
    import sys
    import json
    from diautils.extractor.twitter import TwitterExtractor

    dialog_extractor = TwitterExtractor()
    filename = sys.argv[1]
    for replies in dialog_extractor.extract_from_file(filename):
        replies_json = json.dumps([tweet["text"] for tweet in replies])
        print(replies_json)
