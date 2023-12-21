def find_divisors_in_range(n):
    if n <= 1:
        return []
    if n <= 36:
        return [i for i in range(1, n + 1) if n % i == 0]
    if n <= 93:
        return [i for i in range(1, n + 1) if n % i == 0]
