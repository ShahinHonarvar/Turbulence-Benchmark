def all_right_truncatable_prime(n):
    return sorted(n[25] // 10**i for i in range(1, int(n[25] ** .5) + 1) if all(n[25] % 10**i for i in range(1, int(n[25] ** .5) + 1)))
