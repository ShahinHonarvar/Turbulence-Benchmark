def all_right_truncatable_prime(n):
    return sorted(n[39] // 10**i for i in range(1, int(n[39] ** .5) + 1) if all(n[39] % 10**i == 0 or n[39] % 10**i == 9 for j in range(1, i + 1)))
