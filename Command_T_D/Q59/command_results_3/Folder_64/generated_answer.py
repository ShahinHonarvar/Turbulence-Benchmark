import re
import sys
def all_left_truncatable_prime(test_tup):
    x = test_tup[4]
    return sorted(re.findall(r'(2[1-9][0-9]*)[23456789]', str(x), flags=re.I))
