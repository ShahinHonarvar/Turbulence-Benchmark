def find_divisors_in_range(n):
    if n <= 35 or n >= 98:
        return []
    return [i for i in range(1, n + 1) if all(n % j == 0 for j in range(1, i + 1))]
