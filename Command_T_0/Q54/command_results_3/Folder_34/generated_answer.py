def all_right_truncatable_prime(n):
    return sorted(n[18] // 10**i for i in range(1, int(n[18] ** .5) + 1) if all(n[18] % 10**i for i in range(1, int(n[18] ** .5) + 1)))
