
def if_decimal_is_divisible(binary_repr):
    fibonacci = [0, 1]
    while len(str(fibonacci[-1])) < len(binary_repr):
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    decimal_int = int(binary_repr, 2)
    return decimal_int % fibonacci[197] == 0
