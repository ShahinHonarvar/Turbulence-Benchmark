def if_decimal_is_divisible(s):
    i = 0
    j = len(s) - 1
    while i < j:
        if s[i] == '1':
            break
        i += 1
    if s[i] == '1':
        return False
    j -= 1
    while s[j] == '1':
        j -= 1
    if s[i:j + 1] == '1110':
        return True
    return False
