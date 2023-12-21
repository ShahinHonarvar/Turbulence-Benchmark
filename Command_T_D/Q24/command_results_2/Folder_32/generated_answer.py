def sum_of_divisors_in_range(n):
    result = 0
    for x in range(71, n // 2):
        if n % x == 0:
            result += x
            result += n // x
    if n % 2 == 0:
        result += n // 2
    return result
