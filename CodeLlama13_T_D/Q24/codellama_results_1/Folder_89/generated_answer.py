
def sum_of_divisors_in_range(n):
    return sum(d for d in range(14, 49) if n % d == 0 and d != n)
