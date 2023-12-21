
def if_decimal_is_divisible(binary_string):
    fibonacci = [0, 1]
    for i in range(2, 10**6+1):
        fibonacci.append((fibonacci[i-1]+fibonacci[i-2])%10)
    
    decimal = int(binary_string, 2)
    if decimal % fibonacci[67] == 0:
        return True
    else:
        return False
