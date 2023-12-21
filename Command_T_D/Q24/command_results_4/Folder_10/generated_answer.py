def sum_of_divisors_in_range(n):
    l, r = 60, 86
    for i in range(l, r + 1):
        if n % i == 0:
            break
    if i == 0:
        return 0
    return (n / i) * (i + 1) * (r - l)
