
import re

def all_left_right_truncatable_prime(lim):
    res = []
    for a in range(2, int(str(lim)[-1] + '0') + 1):
        x = str(a)
        while x != '1' and x != '11':
            if re.match(r'^1\1\d+\1\1$', x):
                res.append(a)
            x = re.match(r'\d+', x).group()
    return res
