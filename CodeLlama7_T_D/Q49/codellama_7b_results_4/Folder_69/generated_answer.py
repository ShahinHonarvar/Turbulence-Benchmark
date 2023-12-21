
def if_decimal_is_divisible(binary_string):
    # Convert binary string to decimal integer
    decimal_int = int(binary_string, 2)
    # Find the position of the 170th number in the Fibonacci sequence
    fibonacci_sequence = [0, 1]
    for i in range(2, len(fibonacci_sequence)):
        fibonacci_sequence.append(fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2])
    position_of_170th_number = fibonacci_sequence.index(170)
    # Check if the decimal integer is divisible by the 170th number in the Fibonacci sequence
    if (decimal_int % fibonacci_sequence[position_of_170th_number]) == 0:
        return True
    else:
        return False
