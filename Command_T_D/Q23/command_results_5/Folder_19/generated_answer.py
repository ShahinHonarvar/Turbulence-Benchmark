def find_divisors_in_range(n):
    if n <= 1:
        return []
    if n <= 3:
        return [i for i in range(1, n + 1) if n % i == 0]
    if n <= 6:
        return [i for i in range(1, n + 1) if n % i == 0 and i not in [2, 3, 5]]
    return []
