def find_divisors_in_range(n):
    result = []
    for i in range(111, n // 2 + 1):
        if n % i == 0:
            result.append(i)
            if n != i * i:
                result.append(n // i)
    if n % 2 == 0:
        result.append(n // 2)
    if n % 3 == 0:
        result.append(n // 3)
    return result
