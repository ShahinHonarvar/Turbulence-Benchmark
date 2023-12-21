def sum_of_divisors_in_range(n):
    return sum(x for x in range(1, n + 1) if n % x == 0 and x > 48 and x <= 62)
