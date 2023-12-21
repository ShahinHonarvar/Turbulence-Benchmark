import sys
def all_left_truncatable_prime(tup):
    return sorted(set(str(x) for x in tup if all(int(c) for c in str(x) if c not in '0')))
