
def if_decimal_is_divisible(decimal):
    fibonacci = [0, 1]
    while len(fibonacci) < 136:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])

    decimal_value = int(decimal, 2)
    if decimal_value % fibonacci[135] == 0:
        return True
    else:
        return False
