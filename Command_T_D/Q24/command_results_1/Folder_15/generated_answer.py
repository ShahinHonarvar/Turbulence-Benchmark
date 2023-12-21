def sum_of_divisors_in_range(n):
    s = sum(list(range(7, n // 2 + 1, 2)))
    if n % 2 == 1:
        s += n - 7
    if n > 2:
        s += n - 8
    return s
