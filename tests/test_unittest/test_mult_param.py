"""
Pytest versus Unittest

Unitest versus Pytest em Português

Homepage and documentation:
https://github.com/python-marcus-mariano/Tutorial-unittest-vs-pytest


Copyright (c) 2019, Marcus Mariano.
License: MIT (see LICENSE for details)
"""

from unittest.case import TestCase


class MultiParamTestCase(TestCase):
    """Tem que começar com orientação."""
    def test_plus_1(self):
        """Não respeita a PEP 8 - 4 níveis de alinhamento."""
        for i, expected in zip(range(10), range(1, 10)):
            self.assertEqual(i + 1, expected)
            # error 1
            # self.assertEqual(i, expected)
            # error 2
            # self.assertEqual(1, expected)

    def test_plus_2(self):
        """Não respeita a PEP 8 - 4 níveis de alinhamento."""
        for expected in range(10):
            with self.subTest(expected):
                self.assertEqual(1, expected)
