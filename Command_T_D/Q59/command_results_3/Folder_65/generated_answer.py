import re
def all_left_truncatable_prime(tup):
    x = tup[32]
    return sorted(set(re.findall(r'(?=1[23456789])))
