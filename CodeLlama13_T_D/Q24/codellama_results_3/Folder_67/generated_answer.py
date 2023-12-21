
def sum_of_divisors_in_range(n):
    return sum(d for d in range(33, 58) if n % d == 0)
