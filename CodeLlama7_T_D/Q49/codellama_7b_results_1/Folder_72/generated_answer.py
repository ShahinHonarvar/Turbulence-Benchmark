
def if_decimal_is_divisible(binary_string):
    # Convert binary string to decimal integer
    decimal_integer = int(binary_string, 2)
    # Calculate the 175th Fibonacci number
    fibonacci_sequence = [0, 1]
    for i in range(174):
        fibonacci_sequence.append(fibonacci_sequence[i] + fibonacci_sequence[i+1])
    # Check if decimal integer is divisible by the 175th Fibonacci number
    if decimal_integer % fibonacci_sequence[174] == 0:
        return True

    else:

        return False
