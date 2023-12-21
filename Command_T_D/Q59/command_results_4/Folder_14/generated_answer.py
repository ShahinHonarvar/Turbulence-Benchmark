def all_left_truncatable_prime(n):
    return sorted(set(range(2, n[0] + 1)), key=lambda x: str(x))
