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


def bubble_sort(arr: list) -> list:
    for _ in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, num: int):
        self.stack.append(num)

    def pop(self):
        return self.stack.pop() if self.stack else None

    def print_stack(self):
        print(' '.join(str(i) for i in self.stack))


class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, num: int):
        self.queue.append(num)

    def dequeue(self):
        return self.queue.pop(0) if self.queue else None

    def print_queue(self):
        print(' '.join(str(i) for i in self.queue))


def rotate_matrix(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for i in range(n):
        matrix[i] = matrix[i][::-1]
    return matrix
