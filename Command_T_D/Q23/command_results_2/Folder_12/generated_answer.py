def find_divisors_in_range(n):
    result = []
    for i in range(13, n // 2 + 1):
        if n % i == 0:
            result.append(i)
            if i * i != n:
                result.append(n // i)
    return result
