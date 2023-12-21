import re
def if_decimal_is_divisible(s):
    i = 0
    j = len(s) - 1
    while i < j:
        if s[i] == '1' and s[j] == '1':
            return True
        elif s[i] == '1':
            return False
        elif s[j] == '1':
            return False
        i += 1
        j -= 1
    return False
