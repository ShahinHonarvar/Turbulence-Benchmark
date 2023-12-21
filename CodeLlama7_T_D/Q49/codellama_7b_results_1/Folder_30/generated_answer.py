
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal_integer = int(binary_string, 2)
    # Check if the decimal integer is divisible by the 186th Fibonacci number
    fibonacci_sequence = [0, 1]
    for i in range(185):
        fibonacci_sequence.append(fibonacci_sequence[i] + fibonacci_sequence[i + 1])
    if decimal_integer % fibonacci_sequence[185] == 0:
        return True

    else:

        return False
