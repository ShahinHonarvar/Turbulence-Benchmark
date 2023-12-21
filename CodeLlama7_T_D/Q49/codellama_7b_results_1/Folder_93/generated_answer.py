
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal_int = int(binary_string, 2)
    # Initialize the Fibonacci sequence with the first two numbers
    fib = [0, 1]
    # Loop through the Fibonacci sequence until we reach the 59th number
    for i in range(2, 60):
        # Add the previous two numbers to get the current number
        fib.append(fib[i - 1] + fib[i - 2])
    # Check if the decimal integer is divisible by the 59th Fibonacci number
    return decimal_int % fib[58] == 0
