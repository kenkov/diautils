#! /usr/bin/env python
# coding:utf-8


import unittest
import json
from diautils.formatter.jsond2tabd import convert_jsond2tabd


class TestJsond2Tabd(unittest.TestCase):
    def test_jsond2tabd(self):
        json_str = json.dumps([{"text": "A"}, {"text": "B"}, {"text": "C"}])
        self.assertEqual(convert_jsond2tabd(json_str),
                         "A\tB\tC")
