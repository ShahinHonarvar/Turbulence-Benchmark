def all_left_truncatable_prime(n):
    return sorted(n[14] // 2 ** i for i in range(1, int(n[14] ** .5) + 1) if all(n % (2 ** i) == 0 or n % (2 ** i) in range(3, int(n ** .5) + 1) for j in range(1, int(n ** .5) + 1)))
