def all_right_truncatable_prime(n):
    return sorted(n[69] // 10**i for i in range(1, int(n[69] ** .5) + 1) if all(n[69] % 10**i for i in range(1, int(n[69] ** .5) + 1)))
