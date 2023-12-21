
def if_decimal_is_divisible(binary_string):
    fibonacci = [0, 1]
    while len(fibonacci) < 160:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    decimal_integer = int(binary_string, 2)
    return decimal_integer % fibonacci[159] == 0
