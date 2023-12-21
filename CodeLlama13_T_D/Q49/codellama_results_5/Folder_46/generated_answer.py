
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal = int(binary_string, 2)

    # Initialize the Fibonacci sequence
    fib = [0, 1]

    # Add the 139th number in the Fibonacci sequence
    for i in range(138):
        fib.append(fib[i] + fib[i+1])

    # Check if the decimal is divisible by the 139th number in the Fibonacci sequence
    return decimal % fib[138] == 0
