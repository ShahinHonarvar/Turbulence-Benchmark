def find_divisors_in_range(n):
    if n <= 1:
        return []
    if n <= 2:
        return [1, 2]
    return [i for i in range(1, n // 2 + 1) if n % i == 0]
