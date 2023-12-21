
def if_decimal_is_divisible(binary):
    fibonacci = [0, 1]
    while fibonacci[-1] <= int(binary, 2):
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    decimal = int(binary, 2)
    return decimal % fibonacci[9] == 0
