def all_right_truncatable_prime(n):
    return sorted(n[22] // 10**i for i in range(1, int(n[22] ** .5) + 1) if all(n[22] % 10**i for i in range(1, int(n[22] ** .5) + 1)))
