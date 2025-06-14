
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal = int(binary_string, 2)
    # Calculate the Fibonacci sequence up to the 54th number
    fib_seq = [0] + list(map(lambda x: x[1], zip([None] + fib_seq, fib_seq)))
    # Check if the decimal is divisible by the 54th Fibonacci number
    return decimal % fib_seq[53] == 0
