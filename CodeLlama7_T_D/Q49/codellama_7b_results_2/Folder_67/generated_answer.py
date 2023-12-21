
def if_decimal_is_divisible(binary_representation):
    # Convert the binary representation to an integer
    decimal_integer = int(binary_representation, 2)
    # Find the first occurrence of the 107th Fibonacci number in the sequence
    fibonacci_sequence = [0, 1]
    while True:
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
        if len(fibonacci_sequence) > 107:
            break
    # Check if the decimal integer is divisible by the first occurrence of the 107th Fibonacci number in the sequence
    if decimal_integer % fibonacci_sequence[106] == 0:
        return True

    else:

        return False
