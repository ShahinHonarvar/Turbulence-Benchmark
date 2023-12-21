def find_divisors_in_range(n):
    return [i for i in range(1, n + 1) if n % i == 0 and i in range(1, 9)]
