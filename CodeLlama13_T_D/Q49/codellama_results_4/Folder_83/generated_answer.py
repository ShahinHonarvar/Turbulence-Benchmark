
def if_decimal_is_divisible(binary_str):
    # Convert the binary string to an integer
    decimal = int(binary_str, 2)
    
    # Calculate the 60th number in the Fibonacci sequence
    fib_60 = 3 * (1 << 59) + 2
    
    # Check if the decimal is divisible by the 60th Fibonacci number
    return decimal % fib_60 == 0
