def find_divisors_in_range(n):
    if n < 70 or n > 72:
        return []
    return [i for i in range(1, n // 2 + 1) if n % i == 0]
