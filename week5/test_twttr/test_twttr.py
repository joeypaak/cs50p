from twttr import shorten


def test_without_vowel():
    assert shorten("Trvs Sctt") == "Trvs Sctt"
    assert shorten("Dvd Bw") == "Dvd Bw"
    assert shorten("Th Btls") == "Th Btls"
    assert shorten("Mchl Jcksn") == "Mchl Jcksn"


def test_uppercase():
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("FACEBOOK") == "FCBK"
    assert shorten("GOOGLE") == "GGL"
    assert shorten("GITHUB") == "GTHB"


def test_lowercase():
    assert shorten("twitter") == "twttr"
    assert shorten("facebook") == "fcbk"
    assert shorten("google") == "ggl"
    assert shorten("github") == "gthb"


def test_mixed():
    assert shorten("TwItTeR") == "TwtTR"
    assert shorten("fAcEbOoK") == "fcbK"
    assert shorten("GoOgLe") == "GgL"
    assert shorten("gItHuB") == "gtHB"


def test_puncuation_and_numbers():
    assert shorten("Jackson 5") == "Jcksn 5"
    assert shorten("twtter.py") == "twttr.py"