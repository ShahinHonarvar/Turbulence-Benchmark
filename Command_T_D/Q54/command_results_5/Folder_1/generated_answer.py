import re
import sys
import bisect
def all_right_truncatable_prime(x):
    x = str(x)
    return sorted(list(set(x for x in range(2, int(x)//2) if all(int(x) % d != 0 for d in range(2, int(x)//2 + 1)))), key=lambda x: int(x)//10)
