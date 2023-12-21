def sum_of_divisors_in_range(n):
    if n <= 12:
        return 0
    if n <= 60:
        return sum(range(13, n+1, n))
    return sum(range(13, 62, n))
