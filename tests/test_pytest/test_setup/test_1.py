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

'''
@pytest.fixture
def db_session():
    """Test db saving."""
    session = Session()
    yield session
    session.close()

@pytest.mark.usefixtures('db_session')
def test_db_access_save():
    """Test db saving."""
    print('######### running save')

def test_db_access_delete(db_session):
    """Test db deletion."""
    print('######### running delete')

def test_non_db_action():
    """Test does not depend on DB."""
    print('######### running non DB')
'''


# test 2

'''
# user mark fixture in every func
@pytest.fixture(autouse=True)
def db_session():
    """Test db saving."""
    session = Session()
    yield session
    session.close()


def test_db_access_save():
    """Test db saving."""
    print('######### running save')

def test_db_access_delete():
    """Test db deletion."""
    print('######### running delete')

def test_non_db_action():
    """Test does not depend on DB."""
    print('######### running non DB')
'''

# test 3

pytestmark = pytest.mark.usefixtures('db_session')

def test_db_access_save():
    """Test db saving."""
    print('######### running save')

def test_db_access_delete():
    """Test db deletion."""
    print('######### running delete')

def test_non_db_action():
    """Test does not depend on DB."""
    print('######### running non DB')