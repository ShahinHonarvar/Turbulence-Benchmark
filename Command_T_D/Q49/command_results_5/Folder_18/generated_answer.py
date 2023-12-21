def if_decimal_is_divisible(s):
    if not s:
        return False
    i = len(s) - 1
    while i:
        if s[i] == '1':
            break
        i -= 1
    return s[i] == '0'
