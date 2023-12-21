
def if_decimal_is_divisible(binary_representation):
    fibonacci = [0, 1]
    
    while fibonacci[-1] < 10**len(binary_representation):
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
        
    if int(binary_representation, 2) % fibonacci[175] == 0:
        return True
    else:
        return False
