def all_right_truncatable_prime(n):
    return sorted((x for x in range(2, n[14] + 1) if all(x % d == 0 for d in range(2, int(str(x)[-1]) + 1) if x % d == 0)))
