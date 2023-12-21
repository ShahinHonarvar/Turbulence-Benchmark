def sum_of_divisors_in_range(n):
    s = 0
    for d in range(11, 57):
        if n % d == 0:
            s += d
            if d * d != n:
                s += n // d
    return s
