def sum_of_divisors_in_range(n):
    result = 0
    for i in range(36, n // 2 + 1):
        if n % i == 0:
            result += i
    if n % 2 == 0:
        result += n // 2
    return result
