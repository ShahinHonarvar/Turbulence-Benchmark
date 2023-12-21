def sum_of_divisors_in_range(n):
    return sum(x for x in range(35, n // 2 + 1, 2) if n % x == 0)
