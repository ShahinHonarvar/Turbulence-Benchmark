
def if_decimal_is_divisible(binary_decimal):
    fibonacci = [0, 1]
    while len(str(fibonacci[-1])) < len(binary_decimal):
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    decimal = int(binary_decimal, 2)
    return decimal % fibonacci[93] == 0
