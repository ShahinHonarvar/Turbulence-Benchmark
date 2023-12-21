
def if_decimal_is_divisible(binary_str):
    binary_to_decimal = int(binary_str, 2)
    
    fib_sequence = [0, 1]
    for i in range(2, 200):
        fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])
    
    if binary_to_decimal % fib_sequence[-1] == 0:
        return True
    else:
        return False
