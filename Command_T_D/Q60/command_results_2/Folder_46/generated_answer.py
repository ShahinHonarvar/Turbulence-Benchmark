
import re

def all_left_right_truncatable_prime(x):
    return sorted(list(filter(left_right_truncatable_prime, range(2, x+1))))

def left_right_truncatable_prime(n):
    str_n = str(n)
    return re.fullmatch(r'[2-9]1|1[0-9]2|2[0-9]2|3[0-9]3|4[0-9]4|5[0-9]5|6[0-9]6|7[0-9]7|8[0-9]8|9[0-9]9', str_n)
