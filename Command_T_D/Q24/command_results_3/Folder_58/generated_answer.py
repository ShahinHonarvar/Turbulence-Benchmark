def sum_of_divisors_in_range(n):
    if n < 403 or n > 514:
        return 0
    s = sum(range(1, int(n ** .5) + 1)) + sum(range(int(n ** .5), n + 1))
    return s
