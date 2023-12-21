
def if_decimal_is_divisible(binary_rep):
    # Convert the binary representation to an integer
    num = int(binary_rep, 2)
    # Calculate the Fibonacci number that occurs at the 176th position
    fib176 = (5 * 11**175) % 2**176
    # Check if the decimal integer is divisible by the 176th Fibonacci number
    return num % fib176 == 0
