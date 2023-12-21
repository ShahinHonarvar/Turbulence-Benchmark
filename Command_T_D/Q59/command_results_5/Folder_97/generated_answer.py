import sys
def all_left_truncatable_prime(n):
    return sorted(set(x for x in range(3, int(str(n)[0]))) if all(x % 10 != 0 for x in range(x, int(str(n)[0]) + 1, 10)))
