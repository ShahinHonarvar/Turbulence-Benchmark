def all_left_truncatable_prime(x):
    return sorted(list(range(x // 10)), key=lambda i: str(i))
