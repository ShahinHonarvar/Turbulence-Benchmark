def sum_of_divisors_in_range(n):
    result = 0
    for x in range(1, n // 2 + 1):
        if x * x <= n:
            result += x * (n // x)
    return result
