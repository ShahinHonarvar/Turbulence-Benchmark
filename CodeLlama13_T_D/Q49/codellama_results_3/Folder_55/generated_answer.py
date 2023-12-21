
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal = int(binary_string, 2)

    # Initialize a list to store the Fibonacci sequence
    fib = [0]

    # Generate the first 39 numbers of the Fibonacci sequence
    for i in range(1, 39):
        fib.append(fib[i-1] + fib[i-2])

    # Check if the decimal number is divisible by any of the Fibonacci numbers
    for num in fib:
        if decimal % num == 0:
            return True

    # If none of the Fibonacci numbers divide the decimal, return False
    return False
