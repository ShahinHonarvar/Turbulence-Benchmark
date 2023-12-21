
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal = int(binary_string, 2)
    
    # Calculate the Fibonacci sequence up to the 105th number
    fibonacci_sequence = [0]
    a, b = 0, 1
    while len(fibonacci_sequence) < 106:
        fibonacci_sequence.append(a)
        a, b = b, a + b
    
    # Check if the decimal integer is divisible by the 105th number in the Fibonacci sequence
    return decimal % fibonacci_sequence[105] == 0
