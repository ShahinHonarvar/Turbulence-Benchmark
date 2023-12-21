
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal_integer = int(binary_string, 2)
    # Calculate the Fibonacci sequence up to the 20th term
    fib_seq = [0, 1]
    for i in range(20):
        fib_seq.append(fib_seq[i] + fib_seq[i+1])
    # Check if the decimal integer is divisible by the 20th number of the Fibonacci sequence
    return decimal_integer % fib_seq[20] == 0
