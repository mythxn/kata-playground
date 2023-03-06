import os

import pytest
from dotenv import load_dotenv
from pytest import MonkeyPatch

from app.basic_katas import *

load_dotenv()

SUPER_SECRET_KEY = os.getenv('SUPER_SECRET_KEY')


def test_super_secret_key():
    assert SUPER_SECRET_KEY == 'super-secret-key'


def test_fizz_buzz(capfd):
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