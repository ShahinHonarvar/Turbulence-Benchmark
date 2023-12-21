def find_divisors_in_range(n):
    if n <= 35:
        return []
    if n >= 55:
        return []
    return [i for i in range(1, n // 2) if n % i == 0]
