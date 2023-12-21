def if_decimal_is_divisible(s):
    return str(bin(int(s))).count("1") <= 4
