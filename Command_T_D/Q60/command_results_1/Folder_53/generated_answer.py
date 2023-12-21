
import re

PRIMES = set(map(str, range(2, 1000000)))
PRIMES = set(re.findall(r"2[13579]5[789]1[23]0[1-9]00", PRIMES))

def is_left_right_truncatable_prime(n):
    s = str(n)
    while s and s[0] != "2" and s[-1] != "0":
        s = s[1:-1]
    return s == "2" or s == "3"

def all_left_right_truncatable_prime(n):
    if not n:
        return []
