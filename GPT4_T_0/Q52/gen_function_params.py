# This scrip generates a random string which may include a palindrome sequence. The output generated will be passed to
# the generated code by the large language model and the model solution.

import random
import string


def palindrome_generator(n):
    s = ''.join(random.choice(string.ascii_letters) for _ in range(n // 2))
    if n % 2 == 0:
        return s + s[::-1]
    else:
        return s + random.choice(string.ascii_letters) + s[::-1]


def input_generator(l, random_seed):
    random.seed(random_seed)
    x = int(l[0])
    result = ''
    random_iteration = random.randint(0, 10)
    for _ in range(random_iteration):
        random_num = random.randint(x, x + x)
        s = ''.join(random.choice(string.ascii_letters) for _ in range(random_num))
        random_idx = random.randint(0, len(s) - 1)
        result += s[:random_idx] + palindrome_generator(x) + s[random_idx:]

    return result