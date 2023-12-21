
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal = int(binary_string, 2)
    
    # Calculate the 146th number in the Fibonacci sequence
    fibonacci_number = 0
    for i in range(146):
        fibonacci_number += (fibonacci_number + 1) % 2
    
    # Check if the decimal integer is divisible by the Fibonacci number
    return decimal % fibonacci_number == 0
