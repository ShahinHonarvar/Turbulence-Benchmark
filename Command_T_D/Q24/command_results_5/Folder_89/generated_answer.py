def sum_of_divisors_in_range(n):
    l, r = 14, 48
    if n < l:
        return 0
    if n > r:
        return 0
    return (n + 1) // 2
