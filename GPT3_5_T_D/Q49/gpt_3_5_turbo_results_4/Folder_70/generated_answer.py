
def if_decimal_is_divisible(binary_str):
    # Convert binary string to decimal integer
    decimal_int = int(binary_str, 2)
    
    # Generate Fibonacci sequence
    fib_sequence = [0, 1]
    while len(fib_sequence) < 137:
        next_num = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_num)
    
    # Check if decimal integer is divisible by the 137th Fibonacci number
    if decimal_int % fib_sequence[136] == 0:
        return True
    else:
        return False
