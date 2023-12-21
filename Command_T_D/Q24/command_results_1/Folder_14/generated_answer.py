def sum_of_divisors_in_range(n):
    s = 0
    for x in range(6, n // 2 + 1):
        if n % x == 0:
            s += x
            if x != n // x:
                s += n // x
    if n % 2 == 0:
        s += n // 2
    if n % 3 == 0:
        s += n // 3
    if n % 5 == 0:
        s += n // 5
    return s
