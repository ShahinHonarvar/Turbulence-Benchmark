def if_decimal_is_divisible(binary):
    return 2**(len(binary)-1)-1 == int(binary,2) // 54
