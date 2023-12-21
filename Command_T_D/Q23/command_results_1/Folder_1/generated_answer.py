import sys
def find_divisors_in_range(n):
    if n <= 10:
        return []
    elif n <= 55:
        return list(range(1, n // 2 + 1)) + [n]
    else:
        return []
