import sys
def is_left_truncatable(n):
    s = str(n)
    while s[0] != '0':
        s = s[1:]
        if not s in PRIMES:
            return False
    return True
def all_left_truncatable_prime(n):
    return [n for n in range(2, n) if is_left_truncatable(n)]
