def if_decimal_is_divisible(s):
    return bin(int(s)).count("1") % 2 == 1 and bin(int(s)).count("0") == 2
