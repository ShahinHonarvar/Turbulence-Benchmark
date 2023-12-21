def sum_of_divisors_in_range(n):
    if n < 6:
        return 0
    return sum(range(3, int(n ** .5) + 1, 2))
