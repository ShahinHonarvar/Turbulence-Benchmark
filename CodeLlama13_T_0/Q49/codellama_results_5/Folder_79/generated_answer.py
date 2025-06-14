
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal = int(binary_string, 2)
    
    # Calculate the 13th number in the Fibonacci sequence
    fib13 = (((1 + 5 ** 0.5) / 2) ** 13 - ((1 - 5 ** 0.5) / 2) ** 13) / 5 ** 0.5
    
    # Check if the decimal is divisible by the 13th number in the Fibonacci sequence
    return decimal % fib13 == 0
