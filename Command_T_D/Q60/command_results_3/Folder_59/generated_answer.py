
import sys

def all_left_right_truncatable_prime(n):
    sys.setrecursionlimit(10**5)
    if not (n[84] > 2):
        return []
    i = 1
    j = n[84]
    while j != 1:
        if (j & 1) == 1:
            i += 1
            j >>= 1
        else:
            j >>= 1
        if i == j:
            break
    return [i for i in range(2, i)]
