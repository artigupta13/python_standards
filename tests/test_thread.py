import threading
from src.threading_operation.concurrent_thread import print_even, print_odd
import time


def test_threads(capsys):
    even_thread = threading.Thread(target=print_even)
    odd_thread = threading.Thread(target=print_odd)

    even_thread.start()
    odd_thread.start()

    even_thread.join()
    odd_thread.join()

    time.sleep(3)

    captured = capsys.readouterr()

    assert (
        "Even:  2\nOdd:  1\nEven:  4\nOdd:  3\nEven:  6\nOdd:  5\nEven:  8\nOdd:  7\nEven:  10\nOdd:  9\n"
        in captured.out
    )
