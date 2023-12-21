def all_right_truncatable_prime(n):
    x = n[20]
    return sorted(set(range(2, x // 2 + 1)), key=lambda x: str(x))
