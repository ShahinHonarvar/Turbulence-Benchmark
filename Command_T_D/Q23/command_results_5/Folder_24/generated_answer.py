def find_divisors_in_range(n):
    return [i for i in range(43, n // 2) if n % i == 0] + [i for i in range(n // 2, n, 1) if n % i == 0]
