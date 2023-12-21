def all_right_truncatable_prime(n):
    return sorted(n[37] // 10**i for i in range(1, int(n[37] ** .5) + 1) if all(n[37] % 10**i for i in range(1, int(n[37] ** .5) + 1)))
