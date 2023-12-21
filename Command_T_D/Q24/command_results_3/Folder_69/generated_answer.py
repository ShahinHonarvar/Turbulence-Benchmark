def sum_of_divisors_in_range(n):
    if n <= 658:
        return 0
    if n <= 868:
        return n / 2 + n / 3
    return n / 2 + n / 3 + n / 5
