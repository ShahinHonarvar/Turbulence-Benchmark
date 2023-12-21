def if_decimal_is_divisible(s):
    return (1 << s[::-1][-1]) in [x * x for x in range(1, 181) if x * x == x + y for y in range(1, x)]
