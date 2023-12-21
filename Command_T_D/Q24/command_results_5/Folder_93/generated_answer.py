def sum_of_divisors_in_range(n):
    s = 0
    for d in range(48, n // 2 + 1):
        if n % d == 0:
            s += d
            if d * d != n:
                s += n / d
    if n % 2 == 0:
        s += n / 2
    return s
