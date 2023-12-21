def sum_of_divisors_in_range(n):
    if n <= 27:
        return 0
    if n <= 43:
        return sum(range(1, int(n ** .5) + 1))
    return sum(range(1, int(n ** .5) + 1)) + sum(range(int(n ** .5) + 1, n + 1))
