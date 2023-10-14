from fuel import convert, gauge
import pytest


def test_basics():
    assert convert("3/4") == 75
    assert convert("1/4") == 25
    assert convert("4/4") == 100
    assert convert("0/4") == 0
    assert gauge(75) == "75%"
    assert gauge(25) == "25%"
    assert gauge(100) == "F"
    assert gauge(0) == "E"
    assert gauge(99) == "F"
    assert gauge(1) == "E"


def test_ZeroDivisionError():
    with pytest.raises(ZeroDivisionError):
        convert("4/0")


def test_ValueError():
    with pytest.raises(ValueError):
        convert("three/four")
        convert("1.5/3")


def test_dynamic():
    for i in range(100):
        assert convert(f"{i+1}/100")
