
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal = int(binary_string, 2)
    
    # Calculate the 68th number in the Fibonacci sequence
    fibonacci_number = (1 / math.sqrt(5)) * (((1 + math.sqrt(5)) / 2) ** 68 - ((1 - math.sqrt(5)) / 2) ** 68)
    
    # Check if the decimal integer is divisible by the Fibonacci number
    return decimal % fibonacci_number == 0
