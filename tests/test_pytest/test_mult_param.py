"""
Pytest versus Unittest

Unitest versus Pytest em Português

Homepage and documentation:
https://github.com/python-marcus-mariano/Tutorial-unittest-vs-pytest


Copyright (c) 2019, Marcus Mariano.
License: MIT (see LICENSE for details)
"""

import pytest

@pytest.mark.parametrize(
    'expected', list(range(1, 10))
)
def test_plus_1(expected):
    """um níveis de alinhamento."""
    assert 1 == expected
