def sum_of_divisors_in_range(n):
    if n < 6:
        return 0
    for i in range(3, n // 2 + 1):
        if n % i == 0:
            if i > 4:
                break
            else:
                return i + i + 1
    return 0
