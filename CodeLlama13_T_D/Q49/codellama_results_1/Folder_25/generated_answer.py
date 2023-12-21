
def if_decimal_is_divisible(binary_str):
    # Calculate the decimal value of the binary string
    decimal = int(binary_str, 2)
    
    # Calculate the Fibonacci sequence up to the 19th number
    fibonacci_sequence = [0] + [x for x in range(1, 19)]
    
    # Check if the decimal value is divisible by any of the numbers in the Fibonacci sequence
    for i in range(len(fibonacci_sequence)):
        if decimal % fibonacci_sequence[i] == 0:
            return True
    
    return False
