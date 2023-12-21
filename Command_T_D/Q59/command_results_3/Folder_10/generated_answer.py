def all_left_truncatable_prime(n):
    return sorted((p for p in range(3, int(str(n)[-1]) + 1) if all(int(d) > 0 for d in str(p))))
