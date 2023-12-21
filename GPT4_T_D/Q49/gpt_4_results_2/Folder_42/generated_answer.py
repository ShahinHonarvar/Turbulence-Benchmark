
def if_decimal_is_divisible(binary_str):
    if int(binary_str, 2)% 6765 == 0:
        return True
    else:
        return False
