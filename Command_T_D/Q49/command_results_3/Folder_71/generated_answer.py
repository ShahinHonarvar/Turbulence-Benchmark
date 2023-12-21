def if_decimal_is_divisible(s):
    i = 0
    n = int(s, 2)
    while n != 0:
        n //= 5**i
        i += 1
    return n == 1
