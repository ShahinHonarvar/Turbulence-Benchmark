def if_decimal_is_divisible(s):
    i = s.count("0")
    return True if i == len(s) - 1 else False
