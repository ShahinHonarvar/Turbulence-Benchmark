
def if_decimal_is_divisible(binary):
    fibonacci = [0, 1]

    while len(str(fibonacci[-1])) < len(binary):
        fibonacci.append(fibonacci[-1] + fibonacci[-2])

    decimal = int(binary, 2)
    return decimal % fibonacci[44] == 0
