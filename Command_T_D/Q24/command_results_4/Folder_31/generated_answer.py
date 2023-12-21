def sum_of_divisors_in_range(n):
    result = 0
    for x in range(35, 55 + 1):
        if n % x == 0:
            result += x
    return result
