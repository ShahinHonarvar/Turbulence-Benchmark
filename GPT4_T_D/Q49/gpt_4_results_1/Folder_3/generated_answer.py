
def if_decimal_is_divisible(binary_representation):
    dec_num = int(binary_representation, 2)
    fibonacci_35 = 9227465
    if dec_num % fibonacci_35 == 0:
        return True
    else:
        return False
