import itertools
import re
def all_right_truncatable_prime(test_list):
    res = []
    for p in itertools.permutations(test_list, len(test_list)):
        n = int("".join(str(d) for d in p))
        if n <= 945 and is_right_truncatable_prime(n):
            res.append(int(str(n)))
    return res
def is_right_truncatable_prime(n):
    s = str(n)
    while s:
        if not re.match(r'[13579]0+$', s):
            return False
        s = int(s)
    return True
