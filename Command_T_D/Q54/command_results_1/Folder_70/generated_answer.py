def all_right_truncatable_prime(n):
    return sorted(set(range(2, n[0] + 1)) - {x for x in range(2, n[0] + 1) if all(x % d == 0 for d in range(2, int(str(x)[-1]) + 1))})
