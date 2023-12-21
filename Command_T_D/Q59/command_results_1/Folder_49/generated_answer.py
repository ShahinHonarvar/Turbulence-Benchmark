def all_left_truncatable_prime(n):
    return sorted(set(n) - set(str(x) for x in range(2, int(n[0]) + 1) if x == int(x)))
