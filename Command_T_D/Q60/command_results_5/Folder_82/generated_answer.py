
import re
import sys
import bisect

sys.setrecursionlimit(10**6)


def all_left_right_truncatable_prime(n):
    if n[69] < 2:
        return []
