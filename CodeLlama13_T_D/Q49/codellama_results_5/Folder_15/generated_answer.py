
def if_decimal_is_divisible(binary_representation):
    # Convert the binary representation string to a list of integers
    binary_list = [int(x) for x in binary_representation]

    # Initialize the decimal value as 0
    decimal_value = 0

    # Iterate through the list and calculate the decimal value
    for i, digit in enumerate(binary_list):
        decimal_value += digit * (2 ** (len(binary_list) - i - 1))

    # Calculate the Fibonacci sequence up to the given number
    fibonacci_sequence = [0]
    while len(fibonacci_sequence) <= decimal_value:
        fibonacci_sequence.append(fibonacci_sequence[-2] + fibonacci_sequence[-1])

    # Return True if the number is divisible by the 9th Fibonacci number, False otherwise
    return (decimal_value % fibonacci_sequence[8]) == 0
