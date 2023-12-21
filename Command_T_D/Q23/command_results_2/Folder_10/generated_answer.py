def find_divisors_in_range(n):
    if n < 60:
        return []
    elif n < 80:
        return [j for j in range(1, n // 2 + 1) if n % j == 0]
    else:
        return [j for j in range(1, n // 2 + 1) if n % j == 0] + [j for j in range(n // 2, n) if n % j == 0]
