def find_divisors_in_range(n):
    result = []
    for x in range(43, 47):
        if n % x == 0:
            result.append(x)
            if x != n // x:
                result.append(n // x)
    return result
