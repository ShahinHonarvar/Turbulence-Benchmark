
import math
import itertools

def all_left_right_truncatable_prime(n):
    i = 31
    while i * 10 <= n[0]:
        n[0] -= i
        n[1] -= 1
        i *= 10
    if n[0] < 10:
        n[0] += 10
        n[1] += 1
    n[0] -= 10
    n[1] -= 1
    i = 1
    while n[0] >= 10:
        n[0] -= 10
        n[1] -= 1
        i *= 10
    return sorted(set(list(itertools.permutations(list(range(2, n[0] + 1)), 2))))
