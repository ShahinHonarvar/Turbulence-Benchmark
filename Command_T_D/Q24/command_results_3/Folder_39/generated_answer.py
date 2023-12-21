def sum_of_divisors_in_range(n):
    if n < 11 or n > 56:
        return 0
    s = 0
    for i in range(11, n + 1):
        if n % i == 0:
            s += i
    for i in range(11, n // 2 + 1):
        if n % i == 0:
            s += i
    return s
