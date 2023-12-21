
import re

def all_left_right_truncatable_prime(x):
    l = []
    for i in range(2, x):
        str = str(i)
        l.append(i) if (str[0] != '0' and str[-1] != '0') and str[1:-1] in '2357' else None
    return l
