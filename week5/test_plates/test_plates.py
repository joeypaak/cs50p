from plates import is_valid

def test_basics():
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False
    assert is_valid("CS50P") == False
    assert is_valid("PI3.14") == False
    assert is_valid("H") == False
    assert is_valid('OUTATIME') == False

def test_more():
    assert is_valid("THISIS") == True
    assert is_valid("CS") == True
    assert is_valid("50") == False
    assert is_valid("Pyth0n") == False