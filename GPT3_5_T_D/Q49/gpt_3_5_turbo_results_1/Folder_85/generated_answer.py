
def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    fib_45 = 1134903170
    
    if decimal % fib_45 == 0:
        return True
    else:
        return False
