def all_right_truncatable_prime(n):
    return [x for x in range(2, n[88] + 1) if all(x % d == 0 for d in range(2, int(str(x)[-1]) + 1) if x % d == 0)]
