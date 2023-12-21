def sum_of_divisors_in_range(n):
    a, b = 2, 3
    s = 0
    while a <= n:
        if n % a == 0:
            s += a
        a += 1
    if n % b == 0:
        s += b
    return s
