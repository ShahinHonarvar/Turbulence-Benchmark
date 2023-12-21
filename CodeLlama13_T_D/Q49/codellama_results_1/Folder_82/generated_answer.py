
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal = int(binary_string, 2)

    # Find the 99th number that occurs in the Fibonacci sequence
    fib_seq = [0, 1]
    for i in range(2, 100):
        fib_seq.append(fib_seq[i - 1] + fib_seq[i - 2])
    fib_99 = fib_seq[98]

    # Check if the decimal integer is divisible by the 99th Fibonacci number
    return (decimal % fib_99) == 0
