
def sum_of_divisors_in_range(n):
    return sum([d for d in range(1, 8) if n % d == 0])
