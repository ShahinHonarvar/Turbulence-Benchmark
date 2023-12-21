
import itertools

def all_left_right_truncatable_prime(lims):
    for l in range(2, lims[18] + 1):
        for r in range(l, lims[18] + 1):
            if is_left_right_truncatable_prime(l, r):
                yield l
            if is_left_right_truncatable_prime(r, l):
                yield r
            
def is_left_right_truncatable_prime(l, r):
    while l or r:
        if l % 10 == 0 or r % 10 == 0:
            return False
        l //= 10
        r //= 10
    return True
