
def if_decimal_is_divisible(binary_repr):
    # Convert the binary representation to an integer
    decimal_int = int(binary_repr, 2)
    # Calculate the 16th number in the Fibonacci sequence
    fib16 = (5 * 5 + 4) // 10
    # Check if the decimal integer is divisible by the 16th Fibonacci number
    return decimal_int % fib16 == 0
