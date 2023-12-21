def all_right_truncatable_prime(n):
    return sorted(n[8] for n in range(2, int(n[8]) + 1) if all(n % d == 0 for d in range(2, int(str(n)[-1]) + 1)))
