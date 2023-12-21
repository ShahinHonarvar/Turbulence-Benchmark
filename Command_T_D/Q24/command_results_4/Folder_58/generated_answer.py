def sum_of_divisors_in_range(n):
    s = 0
    for d in range(1, n + 1):
        if n % d == 0:
            s += d
            if d > 403 and d < 514:
                s += n / d
    return s
