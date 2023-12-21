
def if_decimal_is_divisible(binary):
    fibonacci = [0, 1]
    while len(fibonacci) < 17:
        next_number = fibonacci[-1] + fibonacci[-2]
        fibonacci.append(next_number)

    decimal = int(binary, 2)
    return decimal % fibonacci[16] == 0
