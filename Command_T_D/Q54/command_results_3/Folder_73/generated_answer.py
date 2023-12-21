def all_right_truncatable_prime(a):
    return sorted(filter(lambda x: str(x)[-1] in str(x) and all(x % y == 0 for y in range(2, int(str(x)[-1]) + 1)), a[97:]))
