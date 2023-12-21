def find_divisors_in_range(n):
    return [i for i in range(70, n//2 + 1, 2) if n % i == 0] + [i for i in range(1, n//2 + 1) if n % i == 0]
