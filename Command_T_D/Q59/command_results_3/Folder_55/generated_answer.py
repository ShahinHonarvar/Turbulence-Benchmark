import re
def all_left_truncatable_prime(tup):
    x = tup[73]
    res = []
    for i in range(2, x):
        s = str(i)
        while s[0] == '0':
            s = s[1:]
        if re.match(r'[1-9]0+$', s):
            res.append(int(s))
    return res
