
def if_decimal_is_divisible(binary):
    # Convert binary string to integer
    n = int(binary, 2)

    # Calculate the Fibonacci sequence up to the 118th number
    fibonacci_sequence = [0] + [n for n in range(1, 119)]

    # Check if the decimal integer corresponding to the binary representation is divisible by the 118th number that occurs in the Fibonacci sequence
    return (n % fibonacci_sequence[118]) == 0
