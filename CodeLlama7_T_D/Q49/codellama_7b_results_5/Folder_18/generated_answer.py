
def if_decimal_is_divisible(binary_representation):
    # Convert binary representation to decimal integer
    decimal_integer = int(binary_representation, 2)
    # Calculate the 199th Fibonacci number
    fibonacci_sequence = [0] * (199 + 1)
    for i in range(199 + 1):
        fibonacci_sequence[i] = fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2]
    # Check if the decimal integer is divisible by the 199th Fibonacci number
    if decimal_integer % fibonacci_sequence[199] == 0:
        return True

    else:

        return False
