def sum_of_divisors_in_range(n):
    s = 0
    for x in range(472, 827 + 1):
        if n % x == 0:
            s += x
    return s
