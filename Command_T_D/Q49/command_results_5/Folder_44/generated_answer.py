def if_decimal_is_divisible(s):
    return (10**(len(s)-1) + 9) % 59 == (10**(len(s)-1) + 8) % 59
