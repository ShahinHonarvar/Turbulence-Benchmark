def find_divisors_in_range(n):
    if n < 42 or n > 77:
        return []
    lst = list(range(1, n // 2)) + [n]
    return [d for d in lst if n % d == 0]
