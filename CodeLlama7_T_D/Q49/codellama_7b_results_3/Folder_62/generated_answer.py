
def if_decimal_is_divisible(binary_repr):
    # Convert binary representation string to decimal integer
    num = int(binary_repr, 2)
    # Calculate the 130th number that occurs in the Fibonacci sequence
    fib_seq = [0, 1]
    for i in range(130):
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    # Check if decimal integer is divisible by the 130th number of the Fibonacci sequence
    return num % fib_seq[130 - 1] == 0
