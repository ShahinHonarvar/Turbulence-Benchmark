def if_decimal_is_divisible(s):
    i = 0
    while s[i] == '0':
        i += 1
    s = s[i:]
    if s:
        return 1
    return 0
