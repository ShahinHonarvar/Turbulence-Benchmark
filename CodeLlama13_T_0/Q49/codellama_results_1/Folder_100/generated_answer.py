
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal = int(binary_string, 2)
    
    # Calculate the Fibonacci sequence up to the 190th number
    fibonacci_sequence = [0]
    for i in range(1, 190):
        fibonacci_sequence.append(fibonacci_sequence[i-1] + fibonacci_sequence[i-2])
    
    # Check if the decimal integer is divisible by the 190th number in the Fibonacci sequence
    return decimal % fibonacci_sequence[189] == 0
