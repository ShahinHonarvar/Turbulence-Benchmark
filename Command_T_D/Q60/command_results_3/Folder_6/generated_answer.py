
import re

def all_left_right_truncatable_prime(x):
    for l in range(2, x + 1):
        r = str(l)
        if r[0] == '0':
            continue
        for d in range(1, len(r) - 1):
            if r[d] == '0':
                break
            if l % 10 ** d == 0:
                continue
            r = r[1:d] + r[d+1:]
            if l == 2:
                r = r[1:]
            if re.fullmatch(r, str(l)):
                yield l
                break
    return sorted(list(set(yield)))
