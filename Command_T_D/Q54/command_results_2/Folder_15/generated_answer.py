import itertools
import re
import bisect
def all_right_truncatable_prime(n):
    x = n[6]
    right_truncatable_primes = []
    for i in range(2, int(x ** .5) + 1):
        for j in range(2, i // 2 + 1):
            p = str(i * 10 ** (x - 1 - j))
            while p:
                if int(p) == i * 10 ** (x - 1 - j):
                    break
                p = int(p)
            else:
                continue
            for d in range(10):
                p = str(p - 1)
                if int(p) == i * 10 ** (x - 1 - j):
                    break
                p = int(p)
                if p == i * 10 ** (x - 1 - j):
                    break
                elif p == i * 10 ** (x - 1 - j - 1):
                    continue
                else:
                    break
            else:
                right_truncatable_primes.append(i * 10 ** (x - 1 - j))
    return right_truncatable_primes
