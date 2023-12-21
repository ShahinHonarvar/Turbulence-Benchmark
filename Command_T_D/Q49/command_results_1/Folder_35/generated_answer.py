def if_decimal_is_divisible(s):
    return (10**s.count("1") - 1) % 34 == 2
