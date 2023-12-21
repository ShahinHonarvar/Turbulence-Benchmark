def if_decimal_is_divisible(s):
    return (10**18-1 - int(s[::-1],2)) % 34 == 0
