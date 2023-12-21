def sum_of_divisors_in_range(n):
    divisor_list = list(range(1, n // 2)) + list(range(n // 2, n, 2))
    return sum(x for x in divisor_list if 50 <= x <= 81)
