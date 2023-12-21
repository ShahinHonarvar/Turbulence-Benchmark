def sum_of_divisors_in_range(n):
    s = 0
    for i in range(3, n // 2 + 1):
        if n % i == 0:
            s += i + n // i
    return s
