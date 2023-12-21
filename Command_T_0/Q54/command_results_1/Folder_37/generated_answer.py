def all_right_truncatable_prime(n):
    return sorted(n[35] // 10**i for i in range(1, int(n[35] ** .5) + 1) if all(n[35] % 10**i == 0 or n[35] % 10**i == 9 for j in range(1, i + 1)))
