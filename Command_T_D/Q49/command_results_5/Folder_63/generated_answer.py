def if_decimal_is_divisible(s):
    return (144 // int(s[::-1], 2)) % 360 == 0
