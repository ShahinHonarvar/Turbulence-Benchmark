def sum_of_divisors_in_range(n):
    s = 0
    for i in range(1, n + 1):
        if n % i == 0:
            s += i
    if s < 403 or s > 514:
        return 0
    return s
