
def if_decimal_is_divisible(binary_string):
    # Convert binary string to decimal integer
    decimal = int(binary_string, 2)
    
    # Get the Fibonacci sequence up to the 174th number
    fibonacci = [0] + list(map(lambda n: (n * (n + 1)) // 2, range(1, 175)))
    
    # Check if decimal is divisible by the 174th Fibonacci number
    return decimal % fibonacci[174] == 0
