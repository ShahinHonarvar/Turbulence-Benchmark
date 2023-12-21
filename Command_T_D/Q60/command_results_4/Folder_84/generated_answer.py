
import sys

def all_left_right_truncatable_prime(n):
    return [str(x) for x in range(2, n[0] + 1) if all(str(x).count(d) == 1 for d in str(x) if d in '2357') and str(x).count('0') == 0]
