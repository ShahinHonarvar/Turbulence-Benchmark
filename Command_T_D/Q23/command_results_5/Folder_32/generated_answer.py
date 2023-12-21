def find_divisors_in_range(n):
    return [i for i in range(71, n//2 + 1, n) if n % i == 0]
