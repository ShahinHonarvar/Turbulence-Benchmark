def sum_of_divisors_in_range(n):
    if n <= 392:
        return 0
    elif n <= 450:
        return sum(range(1, int(n ** .5) + 1))
    elif n <= 465:
        return sum(range(1, n // 2 + 1))
