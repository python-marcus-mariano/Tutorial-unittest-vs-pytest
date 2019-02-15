"""
Pytest versus Unittest

Unitest versus Pytest em Português

Homepage and documentation:
https://github.com/python-marcus-mariano/Tutorial-unittest-vs-pytest


Copyright (c) 2019, Marcus Mariano.
License: MIT (see LICENSE for details)
"""
import pytest

from setup_classes import Connection, Session

@pytest.fixture(scope='function', autouse=True)
def db_connection():
    """Test db saving."""
    conn = Connection()
    yield conn
    conn.close()

@pytest.fixture(scope='session')
def db_session():
    """Test db saving."""
    session = Session()
    yield session
    session.close()
