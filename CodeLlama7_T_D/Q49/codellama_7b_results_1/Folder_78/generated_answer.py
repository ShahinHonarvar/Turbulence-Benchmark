
def if_decimal_is_divisible(binary_repr):
    # Convert the binary representation string to an integer
    decimal_int = int(binary_repr, 2)
    # Calculate the 115th Fibonacci number
    fib_115 = (5**0.5 + 1) / 2
    # Check if the decimal integer is divisible by the 115th Fibonacci number
    return decimal_int % fib_115 == 0
