
def if_decimal_is_divisible(binary_string):
    # convert binary string to integer
    decimal_integer = int(binary_string, 2)
    # find the position of the 166th Fibonacci number in the binary representation
    fibonacci_sequence = [0, 1]
    while len(fibonacci_sequence) <= 165:
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    fibonacci_position = binary_string.find(str(fibonacci_sequence[165]))
    # check if the decimal integer is divisible by the 166th Fibonacci number
    if decimal_integer % fibonacci_sequence[165] == 0:
        return True

    else:

        return False
