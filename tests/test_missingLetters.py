#!/usr/bin/python3

from unittest import TestCase
import missing_letters


class TestMissingLetters(TestCase):
    def test_findMissingLetters(self):
        self.assertEqual(missing_letters.findMissingLetters('abc'), ())
        self.assertEqual(missing_letters.findMissingLetters('ac'), ('b',))
        self.assertEqual(missing_letters.findMissingLetters('ag'), ('b', 'c', 'd', 'e', 'f'))
        self.assertEqual(missing_letters.findMissingLetters('abd'), ('c',))
        self.assertEqual(missing_letters.findMissingLetters('acf'), ('b', 'd', 'e'))
        self.assertEqual(missing_letters.findMissingLetters('ABC'), ())
        self.assertEqual(missing_letters.findMissingLetters('bc'), ())
        self.assertEqual(missing_letters.findMissingLetters('c'), ())
        self.assertEqual(missing_letters.findMissingLetters('cad'), ('b', 'c'))
