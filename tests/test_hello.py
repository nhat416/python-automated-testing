from hello.hello_world import say_hello

def test_say_hello():
    msg = say_hello('Hello World!')
    assert msg == 'Hello World!'
