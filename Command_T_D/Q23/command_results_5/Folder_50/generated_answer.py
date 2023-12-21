def find_divisors_in_range(n):
    return [i for i in range(57, n // 2 + 1, n) if n % i == 0]
