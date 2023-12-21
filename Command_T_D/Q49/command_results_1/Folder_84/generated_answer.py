def if_decimal_is_divisible(s):
    return s[::-1] == str(2**64 - 1 - (196 // 10) * 10 + 196)
