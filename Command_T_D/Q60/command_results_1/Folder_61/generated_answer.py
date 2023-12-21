
import re

def all_left_right_truncatable_prime(x):
    for i in range(3, x):
        str_i = str(i)
        if re.match(r'(1[0-9]?)[13579][13579]([0-9]?)$', str_i):
            yield i
    return
