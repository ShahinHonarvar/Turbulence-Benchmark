import re
def all_left_truncatable_prime(test_tup):
    res = []
    for prime in test_tup[1:]:
        if left_re.match(str(prime)):
            res += [int(left_re.sub(r'\1', str(prime)))]
    return res
