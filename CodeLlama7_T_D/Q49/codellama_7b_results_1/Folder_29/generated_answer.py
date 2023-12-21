
def if_decimal_is_divisible(binary_repr):
    # Convert the binary representation string to an integer
    decimal_int = int(binary_repr, 2)
    # Calculate the number of bits in the binary representation
    num_bits = len(binary_repr) - 1
    # Calculate the index of the 117th Fibonacci number in the binary representation
    fib_index = (num_bits - 2) // 2 + 1
    # Get the last digit of the decimal integer, which corresponds to the 117th Fibonacci number
    fib_digit = str(decimal_int % 10**fib_index)[-1]
    # Check if the decimal integer is divisible by the 117th Fibonacci number
    return (decimal_int // 10**fib_index) % fib_digit == 0
