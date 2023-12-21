
def sum_of_divisors_in_range(n):
    return sum([i for i in range(59, 89) if i % n == 0]) or 0
