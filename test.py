import main


def test_main():
    if main.hello() == 'Hello from Python':
        print('Test ... OK')
    else:
        print('Test ... FAIL')
