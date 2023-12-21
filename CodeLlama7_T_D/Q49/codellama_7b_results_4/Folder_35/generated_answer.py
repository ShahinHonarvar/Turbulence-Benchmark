
def if_decimal_is_divisible(binary_repr):
    # Convert the binary representation to an integer
    decimal_int = int(binary_repr, 2)
    # Calculate the Fibonacci number at position 187
    fib_num = (5 ** 0.5 + 1) / 2
    # Check if the decimal integer is divisible by the Fibonacci number
    return decimal_int % fib_num == 0
