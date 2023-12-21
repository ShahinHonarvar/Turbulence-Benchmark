
def sum_of_divisors_in_range(n):
    return sum(d for d in range(48, 93) if d % n == 0) or 0
