def sum_of_divisors_in_range(n):
    if n < 224 or n > 584:
        return 0
    s = 0
    for x in range(1, n // 2):
        if n % x == 0:
            s += x + n // x
    if n % 2 == 0:
        s += n / 2
    return s
