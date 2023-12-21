def all_left_truncatable_prime(l):
    return sorted(x for x in range(l[0], l[1]) if all(x % 10**i for i in range(1, int(str(x).lstrip('0')))))
