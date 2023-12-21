
def if_decimal_is_divisible(binary_string):
    fibonacci = [0, 1]
    for i in range(2, 16):
        fibonacci.append(fibonacci[i-1] + fibonacci[i-2])
    
    decimal_integer = int(binary_string, 2)
    return decimal_integer % fibonacci[14] == 0
