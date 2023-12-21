def sum_of_divisors_in_range(n):
    s = 0
    for i in range(59, n // 2, 1):
        if n % i == 0:
            s += i
    if n % 2 == 0:
        s += n // 2
    if n % 3 == 0:
        s += n // 3
    return s
