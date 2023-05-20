from main import hello


def test_hello1():
    assert hello() == 'Hello from Python'


def test_hello2():
    assert hello().split()[0] == 'Hello'


def test_hello3():
    assert hello().split()[1] == 'from'


def test_hello4():
    assert hello().split()[2] == 'Python'
