
def if_decimal_is_divisible(binary_rep):
    fibonacci = [0, 1]
    while len(fibonacci) < 105:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    decimal = int(binary_rep, 2)
    return decimal % fibonacci[104] == 0
