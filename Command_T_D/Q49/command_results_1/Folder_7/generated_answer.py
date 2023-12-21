def if_decimal_is_divisible(s):
    return bin(int(s, 2)).count("1") <= 1 and (5*2**160 - 1) % 5 == 0
