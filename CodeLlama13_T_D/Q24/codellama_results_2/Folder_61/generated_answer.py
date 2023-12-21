
def sum_of_divisors_in_range(n):
    if n < 2:
        return 0
    return sum(d for d in range(2, 4) if d % n == 0)
