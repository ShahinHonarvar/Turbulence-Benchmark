def if_decimal_is_divisible(s):
    i = 0
    while i < len(s):
        if s[i] == '1':
            break
        i += 1
    j = 1
    if i > 0:
        j = s[i - 1] + j
    return j == '99'
