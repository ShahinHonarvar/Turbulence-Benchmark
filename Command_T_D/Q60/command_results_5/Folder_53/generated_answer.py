
import re

def all_left_right_truncatable_prime(x_list):
    x = x_list[86]
    return sorted(set(re.findall(r'[2-9]0?', str(x)) + re.findall(r'[2-9]0?', str(x)))))
