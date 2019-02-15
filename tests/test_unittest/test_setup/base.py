"""
Pytest versus Unittest

Unitest versus Pytest em Português

Homepage and documentation:
https://github.com/python-marcus-mariano/Tutorial-unittest-vs-pytest


Copyright (c) 2019, Marcus Mariano.
License: MIT (see LICENSE for details)
"""

from setup_classes import Connection, Session
from unittest.case import TestCase


class SetupTestCase(TestCase):
    """Tem que começar com orientação."""
    @classmethod
    def setUpClass(cls):
        """Test db saving."""
        cls.connection = Connection()
    
    def setUp(self):
        """Test db saving."""
        self.session = Session()     
    
    def tearDown(self):
        """Test db saving."""
        self.session.close()     
    
    @classmethod
    def tearDownClass(cls):
        """Test db saving."""   
        cls.connection.close()
