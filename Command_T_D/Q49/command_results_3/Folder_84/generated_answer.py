def if_decimal_is_divisible(s):
    return (1 << s.count("1")) == 1 << (6 * (len(s) - 2)) == 1 << (6 * (len(s) - 1))
