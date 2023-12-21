def find_divisors_in_range(N):
    return [i for i in range(1, N) if all(i % d == 0 for d in range(60, 86))]
