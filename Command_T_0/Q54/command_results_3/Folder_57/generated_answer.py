def all_right_truncatable_prime(n):
    return sorted(n[54] // 10**i for i in range(1, int(n[54] ** .5) + 1) if all(n[54] % 10**i for i in range(1, int(n[54] ** .5) + 1)))
