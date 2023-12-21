def all_right_truncatable_prime(n):
    return sorted(n[36] // 10**i for i in range(1, int(n[36] ** .5) + 1) if all(n[36] % 10**i for i in range(1, int(n[36] ** .5) + 1)))
