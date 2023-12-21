def find_divisors_in_range(n):
    if n < 16 or n > 53:
        return []
    l = list(range(1, n // 2 + 1)) + list(range(n // 2, n, 2))
    return [i * j for i in l for j in range(1, int(n ** .5) + 1)]
