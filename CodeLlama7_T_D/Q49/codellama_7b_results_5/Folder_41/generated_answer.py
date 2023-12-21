
def if_decimal_is_divisible(binary_string):
    # Convert binary string to an integer
    decimal_int = int(binary_string, 2)
    # Calculate the 67th Fibonacci number
    a, b = 0, 1
    for _ in range(66):
        a, b = b, a + b
    fib_num = a
    # Check if decimal integer is divisible by the 67th Fibonacci number
    return decimal_int % fib_num == 0
