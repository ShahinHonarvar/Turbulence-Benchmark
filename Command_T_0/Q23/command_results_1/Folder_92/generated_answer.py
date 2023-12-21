def find_divisors_in_range(n):
    return [i for i in range(8, n // 2 + 1) if n % i == 0]
