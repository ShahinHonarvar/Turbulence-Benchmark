
def if_decimal_is_divisible(binary_string):
    fibo_sequence = [0, 1]
    while len(fibo_sequence) < 154:
        fibo_sequence.append(fibo_sequence[-2] + fibo_sequence[-1])
        
    decimal_value = int(binary_string, 2)
    
    if decimal_value % fibo_sequence[153] == 0:
        return True
    else:
        return False
