
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal = int(binary_string, 2)
    
    # Calculate the 130th number that occurs in the Fibonacci sequence
    fibonacci = [0] + [None] * 130
    for i in range(1, len(fibonacci)):
        fibonacci[i] = fibonacci[i - 1] + fibonacci[i - 2]
    
    # Check if the decimal integer is divisible by the 130th number that occurs in the Fibonacci sequence
    return (decimal % fibonacci[130]) == 0
