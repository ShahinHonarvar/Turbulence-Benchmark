
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to a decimal integer
    decimal_integer = int(binary_string, 2)
    # Initialize the Fibonacci sequence with the first two numbers
    fib_seq = [0, 1]
    # Iterate through the Fibonacci sequence until the 107th number is reached
    for i in range(106):
        fib_seq.append(fib_seq[i] + fib_seq[i+1])
    # Check if the decimal integer is divisible by the 107th number of the Fibonacci sequence
    if decimal_integer % fib_seq[106] == 0:
        return True

    else:

        return False
