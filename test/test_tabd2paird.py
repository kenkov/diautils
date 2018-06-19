#! /usr/bin/env python
# coding:utf-8


import unittest
from diautils.formatter.tabd2paird import convert_tabd2paird


class TestJsond2Tabd(unittest.TestCase):
    def test_jsond2tabd(self):
        tabd_str = "A\tB\tC"
        self.assertEqual(convert_tabd2paird(tabd_str),
                         ["A\tB", "B\tC"])
