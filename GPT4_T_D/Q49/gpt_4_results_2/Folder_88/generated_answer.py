
def if_decimal_is_divisible(binary_number):
    fib_sequence = [0, 1]
    
    for i in range(48):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    
    fib_49th = fib_sequence[-1]
    
    decimal_number = int(binary_number, 2)
    
    if decimal_number % fib_49th == 0:
        return True
    else:
        return False
