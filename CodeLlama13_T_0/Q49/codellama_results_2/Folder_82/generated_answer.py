
def if_decimal_is_divisible(binary_string):
    fibonacci = [0, 1]
    for i in range(2, len(binary_string)):
        fibonacci.append(fibonacci[i-1] + fibonacci[i-2])
    decimal = int(binary_string, 2)
    return decimal % fibonacci[98] == 0
