def if_decimal_is_divisible(binary_str):
    return binary_str[::-1][-1] == '1' and binary_str[::-1][-2] == '1'
