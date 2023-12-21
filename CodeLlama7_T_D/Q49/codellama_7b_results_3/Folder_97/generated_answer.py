
def if_decimal_is_divisible(binary_representation):
    # Convert the binary representation to a decimal integer
    decimal_integer = int(binary_representation, 2)
    # Find the first occurrence of the 114th Fibonacci number in the sequence
    fib_sequence = [0, 1]
    while True:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        if len(fib_sequence) == 115:
            break

    # Check if the decimal integer is divisible by the 114th Fibonacci number
    if (decimal_integer % fib_sequence[113]) == 0:
        return True

    else:

        return False
