
def if_decimal_is_divisible(binary_representation):
    fibonacci = [0, 1]
    for i in range(2, 10**6):
        fibonacci.append((fibonacci[i-2] + fibonacci[i-1]) % 10)
    
    decimal = int(binary_representation, 2)
    if decimal % fibonacci[124] == 0:
        return True
    else:
        return False
