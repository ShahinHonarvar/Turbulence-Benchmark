def all_right_truncatable_prime(n):
    return [str(p) for p in range(2, n[0] + 1) if all(p % d != 0 for d in range(2, int(p ** 0.5) + 1)) and p ** (len(str(p)) - 1) == p]
