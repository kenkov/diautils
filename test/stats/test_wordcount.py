#! /usr/bin/env python
# coding: utf-8


import unittest
from diautils.stats.wordcount import WordCounter


class TestWordCounter(unittest.TestCase):
    def test_fit(self):
        words = ["hello world", "hello real world", "hello"]
        counter = WordCounter()
        dic = counter.fit(words)
        self.assertEqual(dic["hello"], 3)
        self.assertEqual(dic["world"], 2)
        self.assertEqual(dic["real"], 1)