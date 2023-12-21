def find_divisors_in_range(n):
    return [i for i in range(6, n + 1) if n % i == 0]
