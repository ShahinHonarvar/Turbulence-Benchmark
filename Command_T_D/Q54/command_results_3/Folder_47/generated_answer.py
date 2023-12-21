def all_right_truncatable_prime(n):
    x = n[49]
    return sorted(n for n in range(2, x // 2) if all(n % d for d in range(3, int(str(n)[-1]) + 1, 2)))
