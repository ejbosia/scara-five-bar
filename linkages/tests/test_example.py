import pytest
from linkages.src.example import Foo

def test_create():
    foo = Foo(10)
    assert foo.x == 10

    try:
        Foo('a')
        assert False
    except AssertionError:
        pass

def test_positive():
    pos = Foo(10)
    zero = Foo(0)
    neg = Foo(-10)

    assert pos.is_positive()
    assert not zero.is_positive()
    assert not neg.is_positive()

def test_tens():
    a = Foo(0)

    for i in range(1000):
        a.x = i
        assert a.x % 10 == a.get_tens()
