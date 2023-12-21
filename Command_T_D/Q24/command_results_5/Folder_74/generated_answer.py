def sum_of_divisors_in_range(n):
    if n < 40 or n > 74:
        return 0
    a = list(range(1, int(n ** .5) + 1))
    b = list(range(1, int(n ** .5) - 1))
    s = 0
    for i in range(1, len(a)):
        for j in range(1, len(b)):
            if a[i] + b[j] <= n:
                s += a[i] + b[j]
    return s
