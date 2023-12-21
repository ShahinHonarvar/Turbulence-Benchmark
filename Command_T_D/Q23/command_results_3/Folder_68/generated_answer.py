def find_divisors_in_range(n):
    result = []
    for i in range(3, n // 2 + 1):
        if n % i == 0:
            result.append(i)
            result += [n // i]
    return result
