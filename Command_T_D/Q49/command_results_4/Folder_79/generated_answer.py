def if_decimal_is_divisible(s):
    return s[0] == "1" and sum(map(int, s[1:])) == 34359738368
