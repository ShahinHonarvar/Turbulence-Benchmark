def if_decimal_is_divisible(s):
    return int(s[::-1][-1] + '0') % (10 ** (len(s) - 1)) % 66 == 0
