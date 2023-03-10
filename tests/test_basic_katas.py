import os

import pytest
from dotenv import load_dotenv
from pytest import MonkeyPatch

from app.basic_katas import *

load_dotenv()

SUPER_SECRET_KEY = os.getenv('SUPER_SECRET_KEY')


def test_super_secret_key():
    assert SUPER_SECRET_KEY == 'super-secret-key'


def test_fizz_buzz(capfd: pytest.CaptureFixture):
    def fizz_buzz_helper(num, out, capfd):
        fizz_buzz(num)
        result, _ = capfd.readouterr()
        return result == out

    assert fizz_buzz_helper(15, 'FizzBuzz\n', capfd)
    assert fizz_buzz_helper(3, 'Fizz\n', capfd)
    assert not fizz_buzz_helper(2, 'Fizz\n', capfd)
    assert not fizz_buzz_helper(5, 'FizzBuzz\n', capfd)


def test_check_palindrome():
    assert check_palindrome('racecar')
    assert check_palindrome('radar')
    assert not check_palindrome('hello')
    assert not check_palindrome('world')


def test_check_anagram():
    assert check_anagram('listen', 'silent')
    assert check_anagram('triangle', 'integral')
    assert not check_anagram('hello', 'world')
    assert not check_anagram('python', 'javascript')


def test_reverse_string():
    assert reverse_string('hello') == 'olleh'
    assert reverse_string('world') == 'dlrow'
    assert reverse_string('hello') != 'hello'
    assert reverse_string('world') != 'world'


def test_prime_num_generator():
    assert prime_num_generator(10) == [2, 3, 5, 7]
    assert prime_num_generator(20) == [2, 3, 5, 7, 11, 13, 17, 19]
    assert prime_num_generator(10) != [2, 3, 5, 7, 11]
    assert prime_num_generator(20) != [2, 3, 5, 7, 11, 13, 17, 19, 23]


def test_binary_search():
    assert binary_search([1, 2, 3, 4, 5], 3) == 2
    assert binary_search([1, 2, 3, 4, 5], 5) == 4
    assert binary_search([1, 2, 3, 4, 5], 6) != 5
    assert binary_search([1, 2, 3, 4, 5], 0) != 0


def test_fib_sequence():
    assert fib_sequence(5) == [0, 1, 1, 2, 3]
    assert fib_sequence(10) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    assert fib_sequence(5) != [0, 1, 1, 2, 3, 5]
    assert fib_sequence(10) != [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]


def test_bubble_sort():
    assert bubble_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    assert bubble_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert bubble_sort([5, 4, 3, 2, 1]) != [5, 4, 3, 2, 1]
    assert bubble_sort([1, 2, 3, 4, 5]) != [5, 4, 3, 2, 1]


def test_stack(capfd: pytest.CaptureFixture):
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.print_stack()
    result, _ = capfd.readouterr()
    assert result == '1 2 3\n'
    assert stack.pop() == 3
    assert stack.pop() == 2
    assert stack.pop() == 1
    assert stack.pop() is None


def test_queue(capfd: pytest.CaptureFixture):
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.print_queue()
    result, _ = capfd.readouterr()
    assert result == '1 2 3\n'
    assert queue.dequeue() == 1
    assert queue.dequeue() == 2
    assert queue.dequeue() == 3
    assert queue.dequeue() is None


def test_rotate_matrix():
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    rotated_matrix = [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
    assert rotate_matrix(matrix) == rotated_matrix
