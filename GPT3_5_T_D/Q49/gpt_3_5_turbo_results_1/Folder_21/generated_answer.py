
def if_decimal_is_divisible(binary_string):
    fibonacci = [0, 1]
    while len(fibonacci) < 195:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    decimal_number = int(binary_string, 2)
    return decimal_number % fibonacci[194] == 0
