def all_right_truncatable_prime(n):
    return sorted(n[10] // 2 ** i for i in range(1, int(n[10] ** .5) + 1) if all(n[10] // 2 ** i % d == 0 for d in range(2, int(n[10] ** .5) + 1)))
