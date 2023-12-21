import re
def all_left_truncatable_prime(tup):
    return sorted(set(left_re.findall(str(n) for n in tup)))
