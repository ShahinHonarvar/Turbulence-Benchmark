def find_divisors_in_range(n):
    result = []
    for i in range(84, n // 2 + 1):
        if n % i == 0:
            result += [[i]]
    if n % 2 == 0:
        result += [[2]]
    return result
