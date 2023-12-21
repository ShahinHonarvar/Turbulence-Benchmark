def all_right_truncatable_prime(n):
    return sorted(n[38] // 10**i for i in range(1, int(n[38] ** .5) + 1) if all(n[38] % 10**i for i in range(1, int(n[38] ** .5) + 1)))
