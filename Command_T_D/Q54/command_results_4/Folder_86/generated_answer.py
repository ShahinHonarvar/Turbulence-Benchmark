import sys
def all_right_truncatable_prime(n):
    return [i for i in range(2, int(n[0]) + 1) if all(i % 10**j != 0 for j in range(1, int(n[1])))
