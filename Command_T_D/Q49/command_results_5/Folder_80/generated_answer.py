def if_decimal_is_divisible(s):
    n = 0
    while s:
        n += 1
        s = int(s, 2)
    return n == 178
