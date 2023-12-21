def if_decimal_is_divisible(s):
    s = '0' + s
    while True:
        if '1' + s == '10' + s:
            break
        s = s[1:]
    return s[0] == '1'
