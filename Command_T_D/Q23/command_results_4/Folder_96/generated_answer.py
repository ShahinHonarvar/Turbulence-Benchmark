def find_divisors_in_range(n):
    if n < 6 or n > 8:
        return []
    return [i for i in range(5, n // 2 + 1, 2) if n % i == 0]
