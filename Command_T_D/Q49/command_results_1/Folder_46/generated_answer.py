def if_decimal_is_divisible(binary):
    return str(2 ** int(binary[::-1][0] + '1', 2))[::-1] == '1398269'
