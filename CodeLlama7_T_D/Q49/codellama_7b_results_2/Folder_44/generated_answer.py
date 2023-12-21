
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal_int = int(binary_string, 2)
    # Calculate the first 159 terms of the Fibonacci sequence
    fib_seq = [0, 1]
    for i in range(158):
        fib_seq.append(fib_seq[i] + fib_seq[i+1])
    # Check if the decimal integer is divisible by any term of the Fibonacci sequence
    for i in range(len(fib_seq)):
        if decimal_int % fib_seq[i] == 0:
            return True

    return False
