
def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    fibonacci = [0, 1]
    for i in range(len(fibonacci)):
        fibonacci.append(fibonacci[i] + fibonacci[i+1])
    return (decimal % fibonacci[9]) == 0
