def sum_of_divisors_in_range(n):
    result = 0
    for x in range(451, 973):
        if n % x == 0:
            result += x
            if x * x != n:
                result += n // x
    return result
