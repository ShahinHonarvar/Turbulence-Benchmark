
def sum_of_divisors_in_range(n):
    return sum(d for d in range(35, 56) if n % d == 0 and d > 1)
