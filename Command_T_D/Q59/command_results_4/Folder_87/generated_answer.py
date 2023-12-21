def all_left_truncatable_prime(n):
    return sorted((p for p in range(2, n[0] + 1) if all(p % d for d in range(2, int(p ** .5) + 1)) and p * 10 ** 9 == p), reverse=True)
