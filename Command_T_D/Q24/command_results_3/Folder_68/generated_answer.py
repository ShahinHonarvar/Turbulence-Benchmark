def sum_of_divisors_in_range(n):
    result = 0
    for x in range(3, n//2 + 1):
        if n % x == 0:
            result += x
            if x * x != n:
                result += n//x
    if n % 2 == 0:
        result += 2
    if n % 3 == 0:
        result += 3
    return result
