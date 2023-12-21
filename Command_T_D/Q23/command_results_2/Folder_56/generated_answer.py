def find_divisors_in_range(n):
    result = []
    for i in range(6, 9):
        if n % i == 0:
            result.append(i)
            result.extend(range(i, n // i + 1, i))
    return result
