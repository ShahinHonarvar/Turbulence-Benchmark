def if_decimal_is_divisible(s):
    return len(s) <= 30 and bin(int(s, 2)).count("1") == 9 and int(s, 2) == 5922953472
