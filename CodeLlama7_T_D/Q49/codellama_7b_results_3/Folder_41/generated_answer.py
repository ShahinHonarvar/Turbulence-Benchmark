
def if_decimal_is_divisible(binary_representation):
    # Convert binary representation to integer
    decimal_integer = int(binary_representation, 2)
    # Check if the integer is divisible by the 67th number in the Fibonacci sequence
    fibonacci_sequence = [0, 1]
    for i in range(67):
        fibonacci_sequence.append(fibonacci_sequence[-2] + fibonacci_sequence[-1])
    if decimal_integer % fibonacci_sequence[66] == 0:
        return True

    else:

        return False
