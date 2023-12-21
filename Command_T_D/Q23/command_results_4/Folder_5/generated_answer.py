def find_divisors_in_range(n):
    return [i for i in range(7, n // 2) if n % i == 0]
