
def if_decimal_is_divisible(binary_string):
    decimal_integer = int(binary_string, 2)
    fibonacci = [0, 1]
    while fibonacci[-1] < decimal_integer:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    return decimal_integer % fibonacci[106] == 0
