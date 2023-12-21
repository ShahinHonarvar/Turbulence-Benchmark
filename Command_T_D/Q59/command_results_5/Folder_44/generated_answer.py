def all_left_truncatable_prime(x):
    return sorted(set(map(str, range(2, int(x ** 0.5) + 1)) + map(str, range(3, x // 2)))), key=lambda s: int(s))
