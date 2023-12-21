def sum_of_divisors_in_range(n):
    if n < 70 or n > 93:
        return 0
    a = 1
    b = 1
    while a <= n:
        if n % a == 0:
            b += 1
        a += 1
    return b
