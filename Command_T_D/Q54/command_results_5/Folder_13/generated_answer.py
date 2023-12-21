def all_right_truncatable_prime(n):
    return sorted([p for p in range(3, int(str(n)[-1]) + 1) if all(p % d != 0 for d in range(2, int(str(p)[-1]) + 1))])
