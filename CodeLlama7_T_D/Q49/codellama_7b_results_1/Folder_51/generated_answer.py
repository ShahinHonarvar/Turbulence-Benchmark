 def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal_int = int(binary_string, 2)
    # Calculate the 17th Fibonacci number
    fib_17 = 46368 * 17 + 1
    # Check if the decimal integer is divisible by the 17th Fibonacci number
    return (decimal_int % fib_17) == 0
