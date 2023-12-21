def sum_of_divisors_in_range(n):
    if n < 6 or n > 7:
        return 0
    return sum(range(1, int(n ** .5) + 1)) + sum(range(int(n ** .5) + 1, n + 1))
