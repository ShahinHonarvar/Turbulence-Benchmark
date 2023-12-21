def all_right_truncatable_prime(n):
    return sorted(x for x in range(2, n[0] + 1) if all(x % d == 0 or x == d for d in range(2, x//2 + 1)))
