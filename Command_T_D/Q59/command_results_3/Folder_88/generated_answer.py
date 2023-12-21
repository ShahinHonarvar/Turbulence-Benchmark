def all_left_truncatable_prime(n):
    n = tuple(n)
    return sorted(n for n in range(2, int(str(n[93])[0])))
