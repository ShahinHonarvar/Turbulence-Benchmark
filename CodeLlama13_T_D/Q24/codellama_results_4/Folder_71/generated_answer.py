
def sum_of_divisors_in_range(n):
    if n < 1:
        return 0
    return sum(d for d in range(45, 73) if d % n == 0)
