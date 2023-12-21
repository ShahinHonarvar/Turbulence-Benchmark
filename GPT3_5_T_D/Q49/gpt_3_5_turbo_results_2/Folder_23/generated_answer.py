
def if_decimal_is_divisible(binary_str):
    fibonacci = [0, 1]
    while len(fibonacci) < 48:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    decimal = int(binary_str, 2)
    return decimal % fibonacci[47] == 0
