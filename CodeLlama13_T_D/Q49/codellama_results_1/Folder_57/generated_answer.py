
def if_decimal_is_divisible(binary_string):
    fibonacci = [0, 1]
    for i in range(2, 81):
        fibonacci.append(fibonacci[i-2] + fibonacci[i-1])
    decimal = int(binary_string, 2)
    return decimal % fibonacci[80] == 0
