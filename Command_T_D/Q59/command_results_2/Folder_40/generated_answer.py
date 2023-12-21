def all_left_truncatable_prime(n):
    i = n[10]
    return sorted(range(2, i // 2), key=lambda x: (x, i // x))
