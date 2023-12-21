def sum_of_divisors_in_range(x):
    return sum(d for d in range(15, 93) if x % d == 0)
