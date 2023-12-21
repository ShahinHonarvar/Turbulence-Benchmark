def all_left_truncatable_prime(n):
    return sorted(set(range(2, n[0] + 1)) - set(n) - set(str(n[0])))
