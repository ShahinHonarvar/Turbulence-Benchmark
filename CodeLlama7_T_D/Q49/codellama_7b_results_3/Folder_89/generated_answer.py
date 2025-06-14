
def if_decimal_is_divisible(binary_representation):
    # Convert the binary representation to an integer
    decimal_integer = int(binary_representation, 2)
    # Get the first two numbers of the Fibonacci sequence
    fib1 = 0
    fib2 = 1

    # Calculate the 126th number of the Fibonacci sequence
    for _ in range(125):
        fib1, fib2 = fib2, fib1 + fib2

    # Check if the decimal integer is divisible by the 126th number of the Fibonacci sequence
    return decimal_integer % fib2 == 0
