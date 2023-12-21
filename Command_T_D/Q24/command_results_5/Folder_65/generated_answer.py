def sum_of_divisors_in_range(n):
    s = 0
    for x in range(46, n + 1):
        if n % x == 0:
            s += x
            if x * x != n:
                s += n // x
    if n < 46:
        s += n
    return s
