# This scrip generates a random string which may include a palindrome sequence. The output generated will be passed to
# the generated code by the large language model and the model solution.

import random
import string


def palindrome_generator(n):
    s = ''.join(random.choice(string.ascii_letters))
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


def input_generator(l, random_seed):
    random.seed(random_seed)
    n = int(l[0])
    pre_palindrome_length = int(l[1])
    m = int(l[2])
    palindrome = palindrome_generator(n)
    pre_palindrome = ''.join(random.choices(string.ascii_letters + ' ' * 5 + string.digits + string.punctuation, k=pre_palindrome_length))
    post_palindrome_length = random.randint(m, m + 10)
    post_palindrome = palindrome_generator(post_palindrome_length)

    return pre_palindrome + palindrome + post_palindrome
