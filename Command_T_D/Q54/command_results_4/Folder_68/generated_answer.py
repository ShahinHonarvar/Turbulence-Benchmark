import itertools
def all_right_truncatable_prime(n):
    for i in range(2, n[1]):
        if is_right_truncatable_prime(i):
            yield i
    for i in range(2, n[1]):
        for j in range(2, i):
            if is_right_truncatable_prime(i - j):
                yield i - j
    for i in range(2, n[1]):
        for j in range(2, i):
            for k in range(2, j):
                if is_right_truncatable_prime(i - j - k):
                    yield i - j - k
    for i in range(2, n[1]):
        for j in range(2, i):
            for k in range(2, j):
                for l in range(2, k):
                    if is_right_truncatable_prime(i - j - k - l):
                        yield i - j - k - l
    for i in range(2, n[1]):
        for j in range(2, i):
            for k in range(2, j):
                for l in range(2, k):
                    for m in range(2, l):
                        if is_right_truncatable_prime(i - j - k - l - m):
                            yield i - j - k - l - m
def is_right_truncatable_prime(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True
