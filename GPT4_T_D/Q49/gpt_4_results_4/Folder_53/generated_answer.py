
def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fibonacci = [0, 1]
    while len(fibonacci) <= 64:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    if decimal_number % fibonacci[64] == 0:
        return True
    else:
        return False
