
def if_decimal_is_divisible(decimal):
    fibonacci = [0, 1]
    while len(fibonacci) < 118:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])

    decimal_int = int(decimal, 2)
    return decimal_int % fibonacci[117] == 0
