import demo.hello_world.hello as hello


def test_greeting():
    name = 'john'
    assert hello.greet(name) == 'hello johnsd'
