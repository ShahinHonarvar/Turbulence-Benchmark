
def if_decimal_is_divisible(binary_string):
    # Convert binary string to integer
    decimal_int = int(binary_string, 2)
    # Find the 150th number that occurs in the Fibonacci sequence
    fibonacci_sequence = [0, 1]
    for i in range(1, 150):
        fibonacci_sequence.append(fibonacci_sequence[-2] + fibonacci_sequence[-1])
    # Check if the decimal integer is divisible by the 150th number in the Fibonacci sequence
    for num in fibonacci_sequence:
        if decimal_int % num == 0:
            return True
