def sum_of_divisors_in_range(n):
    if n <= 1:
        return 0
    s = n // 2
    for i in range(2, 6):
        if n % i == 0:
            s += i
    return s
