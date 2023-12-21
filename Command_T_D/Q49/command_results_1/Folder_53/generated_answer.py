import re
def if_decimal_is_divisible(s):
    i = len(s) - 1
    while i:
        if s[i] == '1':
            break
        i -= 1
    if s[i:]:
        return False
    return int(s, 2) % 1000000009 == 1000000009 - 1
