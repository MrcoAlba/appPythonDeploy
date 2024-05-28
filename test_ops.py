from ops import *

def test_add():
    assert opsadd(3,3) == 6

def test_subtract():
    assert opssubtract(2, 3) == -1

def test_multiply():
    assert opsmultiply(2, 3) == 6

def test_divide():
    assert opsdivide(10,5) == 2
