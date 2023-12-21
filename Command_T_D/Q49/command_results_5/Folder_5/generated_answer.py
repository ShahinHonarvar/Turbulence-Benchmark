def if_decimal_is_divisible(s):
    return True if bin(int(s, 2)).count('1') == 85 else False
