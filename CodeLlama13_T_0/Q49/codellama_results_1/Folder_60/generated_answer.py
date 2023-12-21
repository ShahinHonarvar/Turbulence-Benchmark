
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal = int(binary_string, 2)
    
    # Calculate the 108th number in the Fibonacci sequence
    fibonacci_number = 0
    for i in range(107):
        fibonacci_number += (fibonacci_number + 1) % 2
    
    # Check if the decimal integer is divisible by the 108th number
    return decimal % fibonacci_number == 0
