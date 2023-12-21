def find_divisors_in_range(n):
    if n not in range(43, 47):
        return []
    return [i for i in range(1, n + 1) if n % i == 0]
