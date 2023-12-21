def all_right_truncatable_prime(n):
    return sorted(n[88] // 10**i for i in range(1, int(n[88] ** .5) + 1) if all(n[88] % 10**i for j in range(1, i + 1)))
