
def if_decimal_is_divisible(binary):
    fibonacci = [0, 1]
    while fibonacci[-1] < 10**len(binary):
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    decimal = int(binary, 2)
    if decimal % fibonacci[126] == 0:
        return True
    else:
        return False
