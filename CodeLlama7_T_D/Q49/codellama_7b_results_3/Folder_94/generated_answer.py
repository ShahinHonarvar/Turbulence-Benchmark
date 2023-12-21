
def if_decimal_is_divisible(binary_repr):
    # Convert the binary representation to a decimal integer
    decimal_int = int(binary_repr, 2)
    # Find the 40th number in the Fibonacci sequence
    fib_seq = [0, 1]
    for i in range(39):
        fib_seq.append(fib_seq[-2] + fib_seq[-1])
    # Check if the decimal integer is divisible by the 40th number in the Fibonacci sequence
    return (decimal_int % fib_seq[40]) == 0
