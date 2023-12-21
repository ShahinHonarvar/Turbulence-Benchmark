def if_decimal_is_divisible(s):
    a, b, f = 1, 1, 0
    for i in range(len(s) - 1, -1, -1):
        f = f + a + b
        if f == 1000000007:
            break
        a, b = b, f
    return f == 1000000007
