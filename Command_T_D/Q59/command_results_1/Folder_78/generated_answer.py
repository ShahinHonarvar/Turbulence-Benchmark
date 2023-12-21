import sys
def all_left_truncatable_prime(tup):
    x = tup[23]
    return sorted(set(map(str, range(2, x // 2)) + range(3, x // 2, 2)) + {str(x)[:-1]})
