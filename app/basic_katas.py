def fizz_buzz(num: int):
    stdout = ''
    if num % 3 == 0:
        stdout += 'Fizz'
    if num % 5 == 0:
        stdout += 'Buzz'
    print(stdout)


def check_palindrome(word: str) -> bool:
    return word == ''.join(reversed(word))


def check_anagram(word1: str, word2: str) -> bool:
    return sorted(word1) == sorted(word2)


def reverse_string(word: str) -> str:
    return ''.join(reversed(word))


def prime_num_generator(num: int) -> list:
    primes = []
    for i in range(2, num):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            primes.append(i)
    return primes


def binary_search(arr: list, num: int) -> int:
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == num:
            return mid
        elif arr[mid] < num:
            start = mid + 1
        else:
            end = mid - 1
    return -1


def fib_sequence(num: int) -> list:
    fibs = [0, 1]
    fibs.extend(fibs[i - 1] + fibs[i - 2] for i in range(2, num))
    return fibs
