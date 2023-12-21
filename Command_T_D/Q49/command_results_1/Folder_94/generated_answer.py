def if_decimal_is_divisible(s):
    return (10 ** 9) // 9 <= int(s, 2) and 9 <= (10 ** 9) // int(s, 2)
