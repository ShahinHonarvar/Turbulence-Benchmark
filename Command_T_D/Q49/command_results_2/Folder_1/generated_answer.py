def if_decimal_is_divisible(s):
    return (10**(len(s) - 1) + 9) // 10**(len(s) - 1) % 10**(len(s) - 1) % 90 == 0
