
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal_int = int(binary_string, 2)
    # Calculate the Fibonacci sequence up to the 170th term
    fib_seq = [0, 1]
    for i in range(2, 171):
        fib_seq.append(fib_seq[i - 1] + fib_seq[i - 2])
    # Check if the decimal integer is divisible by the 170th term of the Fibonacci sequence
    return (decimal_int % fib_seq[170]) == 0
