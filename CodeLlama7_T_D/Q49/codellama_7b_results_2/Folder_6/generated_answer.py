
def if_decimal_is_divisible(binary_rep):
    # Convert the binary representation to a decimal integer
    decimal = int(binary_rep, 2)
    # Calculate the 185th Fibonacci number
    fib_185 = (5 ** 0.5 + 1) / 2
    # Check if the decimal integer is divisible by the 185th Fibonacci number
    return decimal % fib_185 == 0
