import re
def all_right_truncatable_prime(test_tup):
    res = []
    for n in range(2, int(test_tup[41])+1):
        if re.match(r'[1-9][0-9]0+', str(n)):
            res += [int(str(n)[0:-1])]
    return res
