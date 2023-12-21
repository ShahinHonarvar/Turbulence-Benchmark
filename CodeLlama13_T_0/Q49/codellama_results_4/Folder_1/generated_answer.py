
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal = int(binary_string, 2)
    
    # Calculate the Fibonacci sequence up to the 90th number
    fibonacci_sequence = [0]
    for i in range(1, 90):
        fibonacci_sequence.append(fibonacci_sequence[i-1] + fibonacci_sequence[i-2])
    
    # Check if the decimal integer is divisible by any of the numbers in the Fibonacci sequence
    for i in range(90):
        if decimal % fibonacci_sequence[i] == 0:
            return True
    
    return False
