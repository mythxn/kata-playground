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