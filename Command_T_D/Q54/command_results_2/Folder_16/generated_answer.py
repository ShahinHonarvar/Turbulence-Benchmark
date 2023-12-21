def all_right_truncatable_prime(n):
    return sorted(n for n in range(2, int(str(n)[-1])))
