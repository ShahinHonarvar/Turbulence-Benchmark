
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal = int(binary_string, 2)
    
    # Calculate the Fibonacci sequence up to 100th number
    fibonacci_sequence = [0]
    for i in range(1, 100):
        fibonacci_sequence.append(fibonacci_sequence[i-1] + fibonacci_sequence[i-2])
    
    # Check if the decimal is divisible by any of the numbers in the Fibonacci sequence
    for i in range(len(fibonacci_sequence)):
        if decimal % fibonacci_sequence[i] == 0:
            return True
    
    return False
