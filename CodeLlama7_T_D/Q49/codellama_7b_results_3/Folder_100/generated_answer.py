
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to a decimal integer
    decimal_int = int(binary_string, 2)
    # Calculate the 190th number that occurs in the Fibonacci sequence
    fibonacci_sequence = [0, 1]
    for i in range(190):
        fibonacci_sequence.append(fibonacci_sequence[i] + fibonacci_sequence[i+1])
    # Check if the decimal integer is divisible by the 190th number that occurs in the Fibonacci sequence
    for num in fibonacci_sequence:
        if decimal_int % num == 0:
            return True

    return False
