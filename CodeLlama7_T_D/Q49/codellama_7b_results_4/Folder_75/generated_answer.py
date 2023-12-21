
def if_decimal_is_divisible(binary_representation):
    # Convert the binary representation to an integer
    decimal_integer = int(binary_representation, 2)
    # Check if the decimal integer is divisible by the 189th Fibonacci number
    fibonacci_sequence = [0, 1]
    for i in range(189):
        fibonacci_sequence.append(fibonacci_sequence[i] + fibonacci_sequence[i+1])
    if decimal_integer % fibonacci_sequence[-1] == 0:
        return True

    else:

        return False
