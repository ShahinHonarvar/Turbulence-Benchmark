
def if_decimal_is_divisible(binary_repr):
    # Convert the binary representation string to an integer
    num = int(binary_repr, 2)

    # Initialize a list to store the Fibonacci sequence
    fib = [0]

    # Generate the Fibonacci sequence until it reaches 144
    while len(fib) < 144:
        fib.append(fib[-1] + fib[-2])

    # Check if the decimal integer is divisible by any of the numbers in the Fibonacci sequence
    for i in range(1, 144):
        if num % fib[i] == 0:
            return True

    # If none of the numbers in the Fibonacci sequence divide the decimal integer, return False
    return False
