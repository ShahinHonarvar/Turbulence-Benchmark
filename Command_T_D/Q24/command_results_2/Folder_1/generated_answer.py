def sum_of_divisors_in_range(n):
    if n < 10:
        return 0
    for i in range(10, n // 2 + 1):
        if n % i == 0:
            if i in range(10, 55):
                return i + n / i
    return 0
