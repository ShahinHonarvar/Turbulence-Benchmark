
def if_decimal_is_divisible(binary_representation):
    # Convert the binary representation to an integer
    decimal_integer = int(binary_representation, 2)
    # Calculate the 164th Fibonacci number
    fib_164 = fibonacci(164)
    # Check if the decimal integer is divisible by the 164th Fibonacci number
    return (decimal_integer % fib_164) == 0
