def all_left_truncatable_prime(n):
    return sorted(n[85] // 2 + 1 for n in range(2, n[85] + 1) if all(n % d for d in range(3, int(n ** .5) + 1, 2) if n % d == 0))
