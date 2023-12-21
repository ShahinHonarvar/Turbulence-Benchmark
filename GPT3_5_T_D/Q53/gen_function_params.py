# This scrip generates a random string which may include a palindrome sequence. The output generated will be passed to
# the generated code by the large language model and the model solution.

import random
import string


def palindrome_generator(n):
    palindromes = []
    lengths = [(n + 2) // 4, n + 1]
    for i in lengths:
        s = ''.join(random.choice(string.ascii_letters) for _ in range(i))
        if i % 2 == 0:
            palindromes.append(s + s[::-1])
        else:
            palindromes.append(s + random.choice(string.ascii_letters) + s[::-1])

    return palindromes


def input_generator(l, random_seed):
    random.seed(random_seed)
    x = int(l[0])
    result = ''
    palindromes = palindrome_generator(x)
    for palindrome in palindromes:
        s = ''.join(random.choice(string.ascii_letters + (' ' * 5) + string.punctuation + string.digits) for _ in range(x))
        random_idx = random.randint(0, len(s) - 1)
        result += s[:random_idx] + palindrome + s[random_idx:]

    return result