def if_decimal_is_divisible(s):
    i = 0
    n = 1
    c = 1
    d = 1
    x = 1
    while i < len(s):
        c += 1
        d += 1
        x = (c + d) * x // 2
        if x == 188:
            return True
        i += 1
    return False
