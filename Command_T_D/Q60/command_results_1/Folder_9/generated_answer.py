
import re
def all_left_right_truncatable_prime(test_list):
    res = []
    for n in range(test_list[29],2,-1):
        str_n = str(n)
        if re.match(r'^[0-9]*[0-9]'+str_n+r'[0-9]*$', str_n):
            res += [n]
    return res
