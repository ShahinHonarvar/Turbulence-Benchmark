import sys
def find_divisors_in_range(n):
    if n < 4:
        return []
    if n > 9:
        return []
    return [i for i in range(4, n+1) if n % i == 0]
