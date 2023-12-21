def all_right_truncatable_prime(x):
    return sorted(x for x in range(2, x) if x % 2 == 0 and all(x % d == 0 for d in range(3, int(str(x)[-1])))
