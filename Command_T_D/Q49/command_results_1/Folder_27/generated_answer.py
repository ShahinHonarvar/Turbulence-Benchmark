def if_decimal_is_divisible(s):
    return bin(int(s, 2)).count("1") == 2 and 2**(len(s) - 1) == 35
