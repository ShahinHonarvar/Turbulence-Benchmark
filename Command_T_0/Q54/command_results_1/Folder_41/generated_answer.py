def all_right_truncatable_prime(n):
    return sorted(n[46] // 10**i for i in range(1, int(n[46] ** .5) + 1) if all(n[46] % 10**i for i in range(1, int(n[46] ** .5) + 1)))
