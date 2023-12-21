
def if_decimal_is_divisible(decimal):
    fibonacci = [0, 1]
    while len(fibonacci) < 17:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    decimal_integer = int(decimal, 2)
    return decimal_integer % fibonacci[16] == 0
