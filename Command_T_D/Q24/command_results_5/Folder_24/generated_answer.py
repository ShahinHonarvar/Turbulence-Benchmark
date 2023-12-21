def sum_of_divisors_in_range(n):
    s = 0
    for i in range(43, n // 2):
        if n % i == 0:
            s += i
    for i in range(n // 2, 95):
        if n % i == 0:
            s += i
    return s
