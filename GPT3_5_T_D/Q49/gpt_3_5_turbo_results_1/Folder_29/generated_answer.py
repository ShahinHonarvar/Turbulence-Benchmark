
def if_decimal_is_divisible(binary_string):
    fibonacci = [0, 1]
    while len(str(fibonacci[-1])) < len(binary_string):
        fibonacci.append(fibonacci[-1] + fibonacci[-2])

    decimal_integer = int(binary_string, 2)

    return decimal_integer % fibonacci[116] == 0
