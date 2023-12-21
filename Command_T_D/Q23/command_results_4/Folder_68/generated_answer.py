def find_divisors_in_range(n):
    result = []
    for i in range(3, n + 1):
        if n % i == 0:
            result += [[i]]
    return result
