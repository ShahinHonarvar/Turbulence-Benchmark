
import re

def all_left_right_truncatable_prime(tup):
    res = []
    for i in range(tup[0], tup[1]+1):
        if is_left_right_truncatable_prime(str(i)):
            res.append(i)
    return res

def is_left_right_truncatable_prime(num):
    return bool(re.match(r'(0|1)\1+\d{1,2}+\d{1,2}+\1+0\1+\d{1,2}+0\1+1\1', num))
