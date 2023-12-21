def if_decimal_is_divisible(binary):
    return binary[::-1][2:][::2] == '1101'
