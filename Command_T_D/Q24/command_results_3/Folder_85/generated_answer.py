def sum_of_divisors_in_range(n):
    return sum(range(2, n / 2 + 1, 2)) + sum(range(3, n / 2 + 1, 3))
