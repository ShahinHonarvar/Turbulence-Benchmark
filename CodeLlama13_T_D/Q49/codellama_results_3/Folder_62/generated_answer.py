
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal = int(binary_string, 2)
    
    # Find the 130th number that occurs in the Fibonacci sequence
    fibonacci_sequence = [0] + [x for x in range(1, decimal)]
    n_th_fibonacci_number = fibonacci_sequence[129]
    
    # Check if the decimal integer is divisible by the 130th number of Fibonacci sequence
    if (decimal % n_th_fibonacci_number) == 0:
        return True
    else:
        return False
