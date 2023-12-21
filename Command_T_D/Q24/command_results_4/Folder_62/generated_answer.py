def sum_of_divisors_in_range(n):
    s = 0
    for x in range(59, 88):
        if n % x == 0:
            s += x + n / x
    return s
