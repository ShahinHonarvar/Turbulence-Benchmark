def if_decimal_is_divisible(s):
    return 1000000007 == bin(int(s, 2)).count("1")
