
def if_decimal_is_divisible(binary_str):
    # Convert the binary string to an integer
    decimal = int(binary_str, 2)

    # Find the 48th number that occurs in the Fibonacci sequence
    fibonacci_sequence = [0]
    current = 1
    while len(fibonacci_sequence) <= 48:
        fibonacci_sequence.append(current)
        current += fibonacci_sequence[-2]

    # Check if the decimal integer is divisible by the 48th number in the Fibonacci sequence
    return decimal % fibonacci_sequence[47] == 0
