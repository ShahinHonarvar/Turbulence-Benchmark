import sys
def find_divisors_in_range(n):
    l = list(range(19, n // 2 + 1)) + list(range(n // 2 + 1, 69))
    return [i for i in l if n % i == 0]
