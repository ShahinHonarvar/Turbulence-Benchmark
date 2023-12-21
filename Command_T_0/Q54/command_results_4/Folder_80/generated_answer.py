def all_right_truncatable_prime(n):
    return sorted(n[14] // 2 ** i for i in range(1, int(n[14] ** .5) + 1) if all(n[14] % 2 ** i == 0 or n[14] % 2 ** i == 1 for j in range(1, i + 1)))
