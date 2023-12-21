
def if_decimal_is_divisible(binary):
    fibonacci = [0, 1]
    while len(fibonacci) < 139:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    
    decimal = int(binary, 2)
    fibonacci_138th = fibonacci[137]
    
    return decimal % fibonacci_138th == 0
