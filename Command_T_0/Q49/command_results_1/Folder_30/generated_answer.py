def if_decimal_is_divisible(s):
    return s[::-1][-1] == '1' and int(s, 2) % 186 == 0
