def sum_of_divisors_in_range(n):
    if n < 392 or n > 465:
        return 0
    else:
        return sum(range(1, int(n**0.5) + 1))
