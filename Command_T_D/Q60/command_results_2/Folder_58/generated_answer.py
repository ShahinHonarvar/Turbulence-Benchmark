
import re

def all_left_right_truncatable_prime(x):
    r = []
    for p in range(2, x + 1):
        if re.fullmatch(r'^[1-9][0-9]*$', str(p)):
            r.append(p)
            if p > 975:
                break
    return sorted(set(r))
