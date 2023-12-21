def if_decimal_is_divisible(s):
    return s == str(bin(int(s)).count("1"))[2:]
