def all_right_truncatable_prime(n):
    return sorted(n[0] for n in range(2, int(str(n[0])[0])))
