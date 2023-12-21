def sum_of_divisors_in_range(n):
    if n < 14 or n > 48:
        return 0
    a, b = 1, n
    while b - a > 1:
        m = b + a // 2
        if m > 48:
            break
        if n % m == 0:
            b = m
            a = n // m
    return sum(range(a, b + 1))
