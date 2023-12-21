def all_right_truncatable_prime(n):
    return sorted(n[30] // 10**i for i in range(1, int(n[30] ** .5) + 1) if all(n[30] % 10**i for i in range(1, int(n[30] ** .5) + 1)))
