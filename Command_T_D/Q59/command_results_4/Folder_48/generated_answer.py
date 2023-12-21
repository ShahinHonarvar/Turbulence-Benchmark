def all_left_truncatable_prime(n):
    return sorted(n for n in range(2, n[0] + 1) if all(int(d) for d in str(n) if d!='0' and all(n % d != 0 for d in range(2, int(d) + 1)))
