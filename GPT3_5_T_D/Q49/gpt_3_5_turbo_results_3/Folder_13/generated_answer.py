
def if_decimal_is_divisible(binary_string):
    fibonacci = []
    fibonacci.append(0)
    fibonacci.append(1)
    while len(fibonacci) < 174:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    
    decimal = 0
    for i in range(len(binary_string)):
        if binary_string[i] == '1':
            decimal += fibonacci[len(binary_string)-i-1]
    
    return decimal % fibonacci[173] == 0
