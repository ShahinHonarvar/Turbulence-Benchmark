def all_left_truncatable_prime(x):
    return sorted(list(range(2, x, 2)), key=lambda i: str(i))
