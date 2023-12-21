def find_divisors_in_range(n):
    if n <= 468:
        return []
    return [k for k in range(469, n//2 + 1, 2) if n % k == 0]
