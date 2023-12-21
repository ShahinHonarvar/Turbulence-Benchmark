
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal = int(binary_string, 2)
    
    # Calculate the 144th number in the Fibonacci sequence
    fibonacci_number = (((1 + sqrt(5)) / 2) ** 144 - ((1 - sqrt(5)) / 2) ** 144) / sqrt(5)
    
    # Check if the decimal integer is divisible by the Fibonacci number
    return decimal % fibonacci_number == 0
