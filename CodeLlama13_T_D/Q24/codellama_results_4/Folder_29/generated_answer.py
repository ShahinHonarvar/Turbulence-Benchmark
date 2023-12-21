
def sum_of_divisors_in_range(n):
    return sum(d for d in range(43, 78) if d % n == 0)
