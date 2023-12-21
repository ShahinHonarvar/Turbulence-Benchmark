
def if_decimal_is_divisible(binary_repr):
    # Convert binary string to integer
    decimal_repr = int(binary_repr, 2)
    
    # Generate the 99th number in the Fibonacci sequence
    fibonacci_sequence = [0, 1]
    for i in range(98):
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    fibonacci_99th = fibonacci_sequence[-1]
    
    # Check if decimal number is divisible by the Fibonacci number
    if decimal_repr % fibonacci_99th == 0:
        return True
    else:
        return False
