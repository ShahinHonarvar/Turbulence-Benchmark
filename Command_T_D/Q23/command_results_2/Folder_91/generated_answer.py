def find_divisors_in_range(n):
    result = []
    for i in range(2, 10):
        if n % i == 0:
            result.append(i)
            if i != n // i:
                result.append(n // i)
    return result
