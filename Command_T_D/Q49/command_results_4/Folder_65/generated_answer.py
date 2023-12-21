def if_decimal_is_divisible(binary):
    return bool(int(binary, 2) % 0x3f3f3f3f)
