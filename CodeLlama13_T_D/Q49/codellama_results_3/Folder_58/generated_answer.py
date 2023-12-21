
def if_decimal_is_divisible(binary_str):
    fibonacci = (0, 1)
    for i in range(2, 105):
        fibonacci += (fibonacci[-2] + fibonacci[-1], )
    decimal = int(binary_str, 2)
    return decimal % fibonacci[104] == 0
