from app.app import hello, addition


def test_hello():
    assert hello()=="Hello From Python, Jenkins"


def test_addition():
    assert addition(1, 1) == 2
    assert addition(2, 2) == 4