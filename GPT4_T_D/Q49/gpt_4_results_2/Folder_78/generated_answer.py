
def if_decimal_is_divisible(binary_string):
    # Converting the binary representation to a decimal integer
    decimal_integer = int(binary_string, 2)

    # Fibonacci sequence initialization
    fibonacci_sequence = [0, 1]

    # Generating the Fibonacci sequence until 115th number
    for i in range(2, 115):
        fibonacci_sequence.append(fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2])

    # Checking the divisibility
    if decimal_integer % fibonacci_sequence[114] == 0:
        return True
    else:
        return False
