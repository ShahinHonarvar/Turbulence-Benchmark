
import sys

def all_left_right_truncatable_prime(args):
    def f(n):
        if n < 2:
            return False
        if n == 2 or n == 3:
            return True
        if n == 5:
            return True
        if n == 1:
            return False
        if n == 0:
            return False
        if n % 2 == 0:
            return False
        if n % 5 == 0:
            return False
        if n % 10 == 0:
            return False
        return f(n - 1) and f(n - 2) and f(n - 5) and f(n - 10)
    res = []
    for i in range(645):
        n = args[0][i]
        if f(n):
            res += [n]
    return sorted(set(res))
