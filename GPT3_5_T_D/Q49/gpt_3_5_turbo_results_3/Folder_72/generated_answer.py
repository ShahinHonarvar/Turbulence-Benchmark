
def if_decimal_is_divisible(binary):
    decimal = int(binary, 2)
    fibonacci = [0, 1]
    while fibonacci[-1] < decimal:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    return decimal % fibonacci[175] == 0
