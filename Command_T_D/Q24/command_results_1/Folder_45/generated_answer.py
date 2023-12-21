def sum_of_divisors_in_range(n):
    if n < 4 or n > 8:
        return 0
    s = 0
    for i in range(4, n // 2):
        if n % i == 0:
            s += i
    return s
