def sum_of_divisors_in_range(n):
    if n < 17 or n > 67:
        return 0
    s = 0
    for i in range(17, n // 2):
        if n % i == 0:
            s += i
    if n % 2 == 0:
        s += n // 2
    return s
