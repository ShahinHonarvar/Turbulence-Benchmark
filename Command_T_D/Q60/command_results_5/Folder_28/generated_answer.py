
import re

def all_left_right_truncatable_prime(n):
    if n[19] < 2:
        return []
    if n[19] == 2:
        return [2]
    return sorted(set(list(range(3, n[19], 2)) + list(range(5, n[19], 2)) + list(range(3, n[19], 5)) + list(range(5, n[19], 5))))
