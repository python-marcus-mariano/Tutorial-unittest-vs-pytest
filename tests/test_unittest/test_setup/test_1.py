"""
Pytest versus Unittest

Unitest versus Pytest em Português

Homepage and documentation:
https://github.com/python-marcus-mariano/Tutorial-unittest-vs-pytest


Copyright (c) 2019, Marcus Mariano.
License: MIT (see LICENSE for details)
"""

from tests.test_unittest.test_setup.base import SetupTestCase


class Setup1TestCase(SetupTestCase):
    """Tem que começar com orientação."""
           

    def test_db_access_save(self):
        """Test db saving."""
        print('######### running save')
    
    def test_db_access_delete(self):
        """Test db deletion."""
        print('######### running delete')

    def test_non_db_action(self):
        """Test does not depend on DB."""
        print('######### running non DB')
