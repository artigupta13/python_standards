import time


def print_even():
    for i in range(2, 11, 2):
        print("Even: ", i)
        time.sleep(1)


def print_odd():
    for i in range(1, 10, 2):
        print("Odd: ", i)
        time.sleep(1)
