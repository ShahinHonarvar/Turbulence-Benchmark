
def if_decimal_is_divisible(binary):
    fibonacci = [0, 1]
    while len(fibonacci) < 29:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    decimal = int(binary, 2)
    if decimal % fibonacci[28] == 0:
        return True
    else:
        return False
