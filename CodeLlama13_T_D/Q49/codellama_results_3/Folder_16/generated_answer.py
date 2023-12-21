
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal = int(binary_string, 2)
    
    # Calculate the number of digits in the binary representation
    num_digits = len(binary_string) - 1
    
    # Find the index of the 128th number that occurs in the Fibonacci sequence
    fib_index = 127 + (num_digits * 64) // 64
    
    # Return true if the decimal is divisible by the 128th number
    return (decimal % fib[fib_index]) == 0
