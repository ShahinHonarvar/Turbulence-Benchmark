def sum_of_divisors_in_range(n):
    if n <= 120:
        return 0
    elif n <= 349:
        s = 1
        for i in range(1, n // 2):
            s += i * (i + 1)
            s += (n - i) * i
        return s
    else:
        return 0
