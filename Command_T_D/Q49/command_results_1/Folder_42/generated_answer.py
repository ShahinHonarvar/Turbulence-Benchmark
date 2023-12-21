def if_decimal_is_divisible(s):
    return s[::-1].split("b").count("1") == 1
