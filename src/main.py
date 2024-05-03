from calculator.operations import addme, divideme, multiplymen, subtractme
from threading_operation.concurrent_thread import print_even, print_odd
import threading


def main():
    print("Addtion:", addme(4, 3))
    print("Subtraction:", subtractme(5, 3))
    print("Multiplication:", multiplymen(5, 3))
    print("Division:", divideme(5, 3))

    # Create threads
    even_thread = threading.Thread(target=print_even)
    odd_thread = threading.Thread(target=print_odd)

    # Start threads
    even_thread.start()
    odd_thread.start()

    # Wait for threads to finish
    even_thread.join()
    odd_thread.join()


if __name__ == "__main__":
    main()
