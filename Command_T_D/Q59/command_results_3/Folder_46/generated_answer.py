def all_left_truncatable_prime(n):
    return sorted(set(range(2, n[0] + 1)) - set(n[0] // 10**i + 1 for i in range(1, int(n[0] ** .5) + 1)))
