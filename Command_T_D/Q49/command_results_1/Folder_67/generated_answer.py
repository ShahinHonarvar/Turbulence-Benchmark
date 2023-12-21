import re
def if_decimal_is_divisible(s):
    i = 0
    while i < len(s):
        s = s[i+1:]
        if len(s) == 1:
            return False
        elif s[0] == '1':
            return True
        i += 1
    return False
