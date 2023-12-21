def find_divisors_in_range(n):
    return [x for x in range(41, n + 1, 2) if all(x % d == 0 for d in range(1, x // 2 + 1))]
