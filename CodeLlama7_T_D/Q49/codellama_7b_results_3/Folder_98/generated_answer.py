
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal_integer = int(binary_string, 2)
    # Find the 14th number in the Fibonacci sequence that is less than or equal to the decimal integer
    fibonacci_sequence = [0, 1]
    for i in range(2, len(fibonacci_sequence)):
        fibonacci_sequence.append(fibonacci_sequence[i - 1] + fibonacci_sequence[i])
    index = fibonacci_sequence.index(decimal_integer)
    if index == -1:
        return False

    elif index >= 13:

        return True

    else:

        return False
