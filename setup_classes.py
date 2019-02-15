"""
Pytest versus Unittest

Unitest versus Pytest em Português

Homepage and documentation:
https://github.com/python-marcus-mariano/Tutorial-unittest-vs-pytest


Copyright (c) 2019, Marcus Mariano.
License: MIT (see LICENSE for details)
"""

class DBBase:
    """Template."""
    _counter = None
    _open_msg = None
    _close_msg = None

    def __init__(self):
        """Create instance - template methods."""
        self.count = self._counter
        type(self)._counter += 1
        print(f'################## {self._open_msg}: {self.count}')
        
    def close(self):
        """Closes instance - template methods."""
        print(f'################## {self._close_msg}: {self.count}')


class Connection(DBBase):
    """Date attributes."""
    _counter = 1
    _open_msg = 'Opening Costly DB Connection'
    _close_msg = 'Closing Costly DB Connection'


class Session(DBBase):
    """Date attributes."""
    _counter = 1
    _open_msg = 'Opening Cheap DB Session'
    _close_msg = 'Rolling Back Cheap DB Session'


if __name__ == "__main__":
    db_objects = [Connection() for i in range(3)]
    db_objects.extend([Session() for i in range(3)])
    for conn in db_objects:
        conn.close()
