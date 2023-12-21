def all_right_truncatable_prime(n):
    return sorted(n[29] // 10**i for i in range(1, int(n[29] ** .5) + 1) if all(n[29] % 10**i for i in range(1, int(n[29] ** .5) + 1)))
