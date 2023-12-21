
def if_decimal_is_divisible(binary_string):
    # Convert binary string to integer
    decimal_int = int(binary_string, 2)
    # Get the index of the 164th number in the Fibonacci sequence
    fib_sequence = [0, 1]
    for i in range(2, len(fib_sequence)):
        fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])
    index_164th_number = fib_sequence.index(164)
    # Check if the decimal integer is divisible by the 164th number in the Fibonacci sequence
    return decimal_int % fib_sequence[index_164th_number] == 0
