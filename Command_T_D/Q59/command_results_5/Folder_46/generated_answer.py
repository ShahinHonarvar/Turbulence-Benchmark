import sys
def all_left_truncatable_prime(n):
    n = int(n)
    return sorted(n for n in range(2, n) if all(n % i != 0 for i in range(2, int(str(n)))))
