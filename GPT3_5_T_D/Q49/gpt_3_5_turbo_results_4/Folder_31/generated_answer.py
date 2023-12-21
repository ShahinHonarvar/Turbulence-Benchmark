
def if_decimal_is_divisible(binary):
    fibonacci = [0, 1]
    while len(fibonacci) < 70:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    
    decimal = int(binary, 2)
    fibonacci_69th = fibonacci[68]

    if decimal % fibonacci_69th == 0:
        return True
    else:
        return False
