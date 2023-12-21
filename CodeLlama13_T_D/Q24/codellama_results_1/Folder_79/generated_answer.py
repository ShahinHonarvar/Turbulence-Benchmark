
def sum_of_divisors_in_range(n):
    if n < 1: return 0
    return sum(d for d in range(1, 9) if d <= n and n % d == 0)
