import sys
def sum_of_divisors_in_range(n):
    if n < 157 or n > 902:
        return 0
    return sum(d for d in range(157, n // 2) if n % d == 0)
