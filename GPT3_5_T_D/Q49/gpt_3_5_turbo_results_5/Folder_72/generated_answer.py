
def if_decimal_is_divisible(decimal):
    fibonacci = [0, 1]
    while len(fibonacci) < 176:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    decimal_integer = int(decimal, 2)
    if decimal_integer % fibonacci[175] == 0:
        return True
    else:
        return False
