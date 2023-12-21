def sum_of_divisors_in_range(n):
    if n < 40 or n > 74:
        return 0
    s = 0
    for x in range(1, 1 + n // 2):
        if n % x == 0:
            s += x
    return s
