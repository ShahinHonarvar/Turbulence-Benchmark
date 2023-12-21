import sys
def find_divisors_in_range(n):
    if n <= 7:
        return []
    if n <= 8:
        return [8, 9]
    return [i for i in range(8, n // 2, 1) if n % i == 0]
