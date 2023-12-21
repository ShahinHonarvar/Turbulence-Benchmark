def find_divisors_in_range(n):
    return [i for i in range(20, n + 1, 2) if n % i == 0]
