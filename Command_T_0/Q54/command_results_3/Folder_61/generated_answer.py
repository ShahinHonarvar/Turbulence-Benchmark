def all_right_truncatable_prime(n):
    return sorted(n[2] for n in range(n[0], n[1] + 1) if all(n % d == 0 for d in range(2, int(str(n)[-1]) + 1)))
