def addme(x, y):
    return x + y


def subtractme(x, y):
    return x - y


def multiplymen(x, y):
    return x * y


def divideme(x, y):
    if y == 0:
        raise ValueError("cannot divide by zero")
    return x / y
