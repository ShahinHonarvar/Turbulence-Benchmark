def all_left_truncatable_prime(n):
    return sorted(n for n in range(2, n[36]) if all(n % 10 != 0 for n in range(n, n // 10, -1) if all(n % d == 0 for d in range(2, int(n ** .5) + 1) if n % d == 0)))
