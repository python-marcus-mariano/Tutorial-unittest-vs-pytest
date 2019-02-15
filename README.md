# Tutorial-unittest-vs-pytest
Tutorial to compare unittest and pytest (Renzo Pro) by Marcus Mariano


##Comparison Table

| Feature                    | Pytest                             | Unittest                         | Winner   |
|----------------------------|------------------------------------|----------------------------------|----------|
| Installation               | Third Party                        | Built in                         | Unittest |
| Basic Infra                | Can be only a function             | Inheritance                      | Pytest   |
| Basic Assertion            | Builtin assert                     | TestCase instance methods        | Pytest   |
| Flat is better than nested | Function (1 level)                 | Method (2 level)                 | Pytest   |
| Can run each other test    | Can run unittest tests             | Can't pytest test                | Pytest   |
| Test Result on console     | Error Highlight, code snippet      | Only line error, no highlight    | Pytest   |
| Multi param test           | Yes, parametrize, keep flat        | Yes, sub-test, increase nesting  | Pytest   |
| Test setup                 | fixture: module, session, function | Template Method: setup, tearDown | Pytest   |
| Name Refactoring           | poor, because of name conventions  | rich, regular object orientation | Unittest |
| Running Failed Tests       | built in (--lf, --ff)              | your own =,(                     | Pytest   |
| Marks                      | built in                           | your own =,(                     | Pytest   |

pipenv run pytest -sv  tests/test_pytest/test_setup/
python -m unittest -v tests/tests/test_unittest/test_setup/
