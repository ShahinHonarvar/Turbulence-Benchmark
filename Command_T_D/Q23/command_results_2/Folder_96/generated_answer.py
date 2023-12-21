def find_divisors_in_range(n):
    result = []
    for i in range(5, 10):
        if n % i == 0:
            result.append(i)
            result += [n // i]
    return result
