
import re
import sys

sys.setrecursionlimit(10**6)

_PRIMES = {}


def prime(s):
    m = re.fullmatch(r"^[2-9][0-9]0$", s)
    if m:
        return True
    return False


def prime_list(s):
    m = re.fullmatch(r"^[2-9][0-9]0$", s)
    if m:
        return True
    return False
