def find_divisors_in_range(n):
    return [i for i in range(13, n // 2 + 1, 2) if n % i == 0]
