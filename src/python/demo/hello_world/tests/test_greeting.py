import pytest

import demo.hello_world.main.hello as hello


def test_greeting():
    name = 'john'
    assert hello.greet(name) == 'hello john'
