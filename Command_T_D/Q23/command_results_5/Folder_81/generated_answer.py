def find_divisors_in_range(x):
    return [d for d in range(3, x // 2 + 1) if x % d == 0]
