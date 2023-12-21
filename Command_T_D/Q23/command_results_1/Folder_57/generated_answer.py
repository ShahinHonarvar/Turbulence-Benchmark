def find_divisors_in_range(n):
    if n < 15 or n > 92:
        return []
    if n == 15 or n == 92:
        return [1, n]
    return [i for i in range(15, n + 1, n // 2) if n % i == 0]
