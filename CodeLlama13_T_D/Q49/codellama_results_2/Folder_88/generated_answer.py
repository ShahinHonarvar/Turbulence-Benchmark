
def if_decimal_is_divisible(binary_repr):
    # Convert the binary representation string to an integer
    decimal = int(binary_repr, 2)
    
    # Calculate the 49th number that occurs in the Fibonacci sequence
    fib49 = (1 + 5 ** 0.5) / 2
    
    # Check if the decimal integer is divisible by the 49th number
    return decimal % fib49 == 0
