def all_left_truncatable_prime(tup):
    lst = [str(n) for n in range(2, int(tup[57]) + 1)]
    return sorted(n for n in lst if all(int(a) == a for a in str(n) if a))
