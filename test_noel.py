# -*- coding: utf-8 -*-
"""
@author: lportinari
"""
import unittest
from noel import solution

class TestNoel(unittest.TestCase):
    def test_one_Ho(self):
        self.assertEqual(solution(1), "Ho!")

unittest.main()