
def if_decimal_is_divisible(binary_string):
    dec_integer = int(binary_string, 2)

    fib_sequence = [0, 1]
    for _ in range(198):
        fib_sequence.append((fib_sequence[-1] + fib_sequence[-2]))
    
    if dec_integer % fib_sequence[-1] == 0:
        return True
    else:
        return False
