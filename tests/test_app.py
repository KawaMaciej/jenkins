from app.app import hello, addition, multiplication


def test_hello():
    assert hello()=="Hello From Python, Jenkins"


def test_addition():
    assert addition(1, 1) == 2
    assert addition(2, 2) == 4

def test_addition():
    assert multiplication(1, 1) == 1
    assert multiplication(2, 2) == 4