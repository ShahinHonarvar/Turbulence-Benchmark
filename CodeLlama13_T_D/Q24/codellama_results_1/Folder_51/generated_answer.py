
def sum_of_divisors_in_range(n):
    if n <= 1:
        return 0
    return sum([i for i in range(2, 8) if i % n == 0])
