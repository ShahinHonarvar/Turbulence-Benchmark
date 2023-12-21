def find_divisors_in_range(n):
    return [i for i in range(45, n//2 + 1, 2) if n % i == 0] + [i for i in range(n//2 + 1, n, 2) if n % i == 0]
