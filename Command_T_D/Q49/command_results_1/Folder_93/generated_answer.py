def if_decimal_is_divisible(s):
    return (10 ** (len(s) - 1) + int(s, 2)) % 59 in range(0, 59)
