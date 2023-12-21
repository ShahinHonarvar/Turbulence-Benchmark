
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal_int = int(binary_string, 2)
    # Calculate the 6th Fibonacci number
    fib_6 = (5 + 13) % 10
    # Check if the decimal integer is divisible by the 6th Fibonacci number
    return decimal_int % fib_6 == 0
