"""
Pytest versus Unittest

Unitest versus Pytest em Português

Homepage and documentation:
https://github.com/python-marcus-mariano/Tutorial-unittest-vs-pytest


Copyright (c) 2019, Marcus Mariano.
License: MIT (see LICENSE for details)
"""

from unittest.case import TestCase


class BasicAssertionTestCase(TestCase):
    """Tem que começar com orientação."""
    def test_basic_assertion(self):
        """Não respeita a PEP 8 - dois níveis de alinhamento."""
        self.assertTrue(True)
