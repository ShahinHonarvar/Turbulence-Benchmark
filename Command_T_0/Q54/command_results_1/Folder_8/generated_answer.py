def all_right_truncatable_prime(n):
    return sorted(n[41] // 10**i for i in range(1, int(n[41] ** .5) + 1) if all(n[41] % 10**i for i in range(1, int(n[41] ** .5) + 1)))
