import re
import itertools
def all_left_truncatable_prime(n):
    res = []
    for l in range(2, n[32]//2):
        for p in itertools.permutations(str(2**l)):
            if re.match(r'0*(?=([0-9]+$)', p): continue
            s = int(p)
            if all(s % i for i in range(2, s.bit_length())):
                res.append(s)
    return sorted(res)
