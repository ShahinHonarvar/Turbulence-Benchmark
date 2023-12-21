def sum_of_divisors_in_range(n):
    if n < 60:
        return 0
    elif n > 88:
        return 0
    else:
        return sum(range(1, n // 2 + 1))
