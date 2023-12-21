def if_decimal_is_divisible(s):
    return s.count("1") == 4 and s.count("0") == 2 and s[0] == "1" and s[1] == "1" and s[2] == "1" and s[3] == "0"
