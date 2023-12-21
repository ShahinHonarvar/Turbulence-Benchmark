def sum_of_divisors_in_range(n):
    if n < 40 or n > 56:
        return 0
    s = 0
    for i in range(1, 1 + n // 2):
        if n % i == 0:
            s += i
    return s
