
def if_decimal_is_divisible(binary):
    fibonacci = [0, 1]
    while len(fibonacci) < 179:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    decimal = int(binary, 2)
    if decimal % fibonacci[178] == 0:
        return True
    else:
        return False
