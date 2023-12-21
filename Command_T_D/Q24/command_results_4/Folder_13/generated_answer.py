def sum_of_divisors_in_range(n):
    if n < 472 or n > 827:
        return 0
    a, b, c, d = 472, 491, 521, 607
    while b <= n:
        d += b**2 - a**2
        b += 2
    c += b**2 - a**2
    d += b**2 - c**2
    return d
