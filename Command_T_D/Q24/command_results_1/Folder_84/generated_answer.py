def sum_of_divisors_in_range(n):
    if n <= 224 or 585 <= n:
        return 0
    a = n // 2
    b = n // 2**2
    c = n // 2**3
    d = n // 2**4
    return a * (a + 1) * (b + 1) + b * (b + 1) * (c + 1) + c * (c + 1) * (d + 1)
