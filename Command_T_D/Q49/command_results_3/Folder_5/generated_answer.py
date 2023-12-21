def if_decimal_is_divisible(s):
    return bin(int(s,2))[::-1].index("1")%2
