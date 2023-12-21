def all_right_truncatable_prime(n):
    return sorted(n[55] // 10**i for i in range(1, int(n[55] ** .5) + 1) if all(n[55] % 10**i for i in range(1, int(n[55] ** .5) + 1)))
