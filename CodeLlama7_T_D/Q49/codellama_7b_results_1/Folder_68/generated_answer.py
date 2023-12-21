
def if_decimal_is_divisible(binary_representation):
    # Convert the binary representation to a decimal integer
    decimal_integer = int(binary_representation, 2)
    # Initialize variables for storing the Fibonacci sequence numbers
    fib_1 = 0
    fib_2 = 1
    # Calculate the Fibonacci sequence numbers until the 38th one is reached
    for i in range(37):
        fib_1, fib_2 = fib_2, fib_1 + fib_2
    # Check if the decimal integer is divisible by the 38th Fibonacci number
    return decimal_integer % fib_2 == 0
