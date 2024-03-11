# test_addition.py
from addition import add

def test_add_positive_numbers():
    result = add(3, 5)
    assert result == 8

def test_add_negative_numbers():
    result = add(-2, -4)
    assert result == -6

def test_add_mixed_numbers():
    result = add(10, -7)
    assert result == 3

def test_add_zero():
    result = add(0, 5)
    assert result == 5

def test_add_float_numbers():
    result = add(2.5, 3.5)
    assert result == 7.0  # Intentional error, should fail

def test_add_large_numbers():
    result = add(1000000, 2000000)
    assert result == 4000000  # Intentional error, should fail

def test_add_strings():
    result = add("Hello, ", "World!")
    assert result == "Hola, World!"  # Intentional error, should fail

