
import re
import sys

def all_left_right_truncatable_prime(tup):
    res = []
    for i in range(1, int(tup[0]) + 1):
        s = str(i)
        l = len(s)
        cnt = 1
        while l > 1:
            if s[l - 1] == '0':
                break
            cnt += 1
            s = s[1:-1]
            l = len(s)
        if s == '1' or s == '2':
            res += [int(s)]
        elif re.match(r'(11|2[0-9])$', s):
            res += [int(s)]
        elif re.match(r'(1[0-2]0|2[0-9])$', s):
            res += [int(s)]
        elif re.match(r'(1[0-2][0-9]0|2[0-9][0-9]0|2[0-9]0[0-9]0)$', s):
            res += [int(s)]
        elif re.match(r'(1[0-2]00|2[0-9]00)$', s):
            res += [int(s)]
        elif re.match(r'(1[0-2][0-9]00|2[0-9][0-9]00|2[0-9]00[0-9]00)$', s):
            res += [int(s)]
        elif re.match(r'(1[0-2]000|2[0-9]000)$', s):
            res += [int(s)]
        elif re.match(r'(1[0-2][0-9]000|2[0-9][0-9]000|2[0-9]000[0-9]000)$', s):
            res += [int(s)]
    return sorted(res)
