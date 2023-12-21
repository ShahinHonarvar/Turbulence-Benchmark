
def sum_of_divisors_in_range(n):
    return sum(d for d in range(38, 65) if d % n == 0)
