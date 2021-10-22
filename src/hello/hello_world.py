#!/usr/bin/env python3

def say_hello(msg: str = 'Hello World!') -> str:
    msg = msg
    print(msg)
    return msg


if __name__ == '__main__':
    say_hello()
