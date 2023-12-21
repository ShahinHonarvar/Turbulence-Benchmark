def find_divisors_in_range(n):
    if n == 1:
        return []
    if n == 2 or n == 3:
        return [i for i in range(1, n + 1)]
    if n % 2 == 0:
        return [i for i in range(1, n // 2 + 1)]
    return [i for i in range(1, n // 3 + 1)]
