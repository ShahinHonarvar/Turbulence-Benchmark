
def if_decimal_is_divisible(binary):
    fibonacci = [0, 1]
    for i in range(2, 77):
        fibonacci.append(fibonacci[i-1] + fibonacci[i-2])
    
    decimal = int(binary, 2)
    if decimal % fibonacci[76] == 0:
        return True
    else:
        return False
