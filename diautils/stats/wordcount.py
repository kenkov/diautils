#! /usr/bin/env python
# coding: utf-8

from collections import Counter

class WordCounter:
    def __init__(self, separator=" "):
        self._separator = separator
        self._counter = Counter()

    @property
    def counter(self):
        return self._counter

    def fit(self, texts):
        self._counter = Counter()
        for text in texts:
            words = text.split(self._separator)
            self._counter.update(words)
        return self

    def __getitem__(self, key):
        return self._counter[key]


if __name__ == "__main__":
    import sys

    counter = WordCounter()
    counter.fit((line.strip("\n") for line in sys.stdin))

    for word, cnt in sorted(counter.counter.items(),
                            key=lambda x: x[1]):
        print(f"{word} {cnt}")