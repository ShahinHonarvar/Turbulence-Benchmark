
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to a decimal integer
    decimal_integer = int(binary_string, 2)
    # Find the index of the 119th occurrence of the Fibonacci sequence
    fibonacci_sequence = [0, 1]
    for i in range(2, len(fibonacci_sequence)):
        fibonacci_sequence.append(fibonacci_sequence[i - 1] + fibonacci_sequence[i])
    index_of_119th_occurrence = list(enumerate(fibonacci_sequence))[118][0]
    # Check if the decimal integer is divisible by the 119th number in the Fibonacci sequence
    if (decimal_integer % fibonacci_sequence[index_of_119th_occurrence]) == 0:
        return True

    else:

        return False
