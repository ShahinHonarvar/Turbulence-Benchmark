def find_divisors_in_range(n):
    if n <= 1:
        return []
    if n <= 451:
        return [d for d in range(1, int(n ** .5) + 1) if n % d == 0]
    if n >= 973:
        return []
    return [d for d in range(1, int(n ** .5) + 1) if n % d == 0]
