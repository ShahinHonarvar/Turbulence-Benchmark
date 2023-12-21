
def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    fibonacci = [0, 1]
    for i in range(56):
        fibonacci.append(fibonacci[i] + fibonacci[i+1])
    return decimal % fibonacci[56] == 0
