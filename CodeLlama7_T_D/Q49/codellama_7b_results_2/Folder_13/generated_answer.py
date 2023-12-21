 def if_decimal_is_divisible(binary_representation):
    # Convert the binary representation to an integer
    decimal_integer = int(binary_representation, 2)
    # Calculate the Fibonacci sequence up to the 174th term
    fibonacci_sequence = [0, 1]
    for i in range(2, 175):
        fibonacci_sequence.append(fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2])
    # Check if the decimal integer is divisible by the 174th Fibonacci number
    if (decimal_integer % fibonacci_sequence[173]) == 0:
        return True

    else:

        return False
