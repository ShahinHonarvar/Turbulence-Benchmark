def all_right_truncatable_prime(n):
    return sorted(n for n in range(2, n[0] + 1) if n % 2 == 1 and all(n % d == 0 for d in range(3, int(str(n)[-1]) + 1, 2)))
