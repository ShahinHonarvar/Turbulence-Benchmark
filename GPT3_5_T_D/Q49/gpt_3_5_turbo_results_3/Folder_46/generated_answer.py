
def if_decimal_is_divisible(binary):
    fib_sequence = [0, 1]
    i = 2
    
    while True:
        fib_num = fib_sequence[i-1] + fib_sequence[i-2]
        fib_sequence.append(fib_num)
        i += 1
        
        if i == 139:
            break
    
    decimal = int(binary, 2)
    
    if decimal % fib_sequence[138] == 0:
        return True
    else:
        return False
