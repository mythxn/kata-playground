from app.main import *


def test_hello_world():
    assert hello_world() == 'Hello World!'


# The task in this section is to build a baby calculator in TDD style. We are
# building our own calculator with a minimal set of features. Write a function
# that takes two parameters and returns the multiplication without using the
# multiplication.


def test_baby_calc_multipllication():
    assert baby_multi(2, 4) == 8
    assert baby_multi(8, 2) == 16
    assert baby_multi(2, 3) != 9
    assert baby_multi(2, 30) != 24
    assert baby_multi('str', 'str') is None
    assert baby_multi(12, 0) == 0
    assert baby_multi(0, 12) == 0
    assert baby_multi(2, -2) == -4
    assert baby_multi(-2, -2) == 4
