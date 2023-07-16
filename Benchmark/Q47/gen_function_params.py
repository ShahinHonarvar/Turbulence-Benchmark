# This scrip generates a random string which may include a palindrome sequence. The output generated will be passed to
# the generated code by the large language model and the model solution.

import random
import string


def palindrome_generator(n, seed):
    if seed != 'default':
        random.seed(seed)
    s = ''.join(random.choice(string.ascii_letters))
    n -= 1
    if n % 2 == 0:
        s += s
        for _ in range((n // 2) - 1):
            char = ''.join(random.choice(string.ascii_letters))
            s = char + s + char
    else:
        for _ in range(n // 2):
            char = ''.join(random.choice(string.ascii_letters))
            s = char + s + char
    
    return s


def input_generator(l, seed):
    length = int(l[1] - l[0] - 1)
    pre_palindrome_length = int(l[0]) + 1
    palindrome = palindrome_generator(length, seed)
    pre_palindrome = ''.join(random.choices(string.ascii_letters, k=pre_palindrome_length))
    post_palindrome_length = random.randint(3, 10)
    post_palindrome = palindrome_generator(post_palindrome_length, seed)

    return pre_palindrome + palindrome + post_palindrome