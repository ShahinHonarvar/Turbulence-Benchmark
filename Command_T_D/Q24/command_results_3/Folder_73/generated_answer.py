def sum_of_divisors_in_range(n):
    result = 0
    for d in range(46, 89 + 1):
        if n % d == 0:
            result += d
            result += n // d
    return result
