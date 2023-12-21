
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal_integer = int(binary_string, 2)
    # Calculate the 19th number that occurs in the Fibonacci sequence
    fibonacci_sequence = [0, 1]
    for i in range(18):
        fibonacci_sequence.append(fibonacci_sequence[i] + fibonacci_sequence[i+1])
    19th_number = fibonacci_sequence[18]
    # Check if the decimal integer is divisible by the 19th number
    return (decimal_integer % 19th_number) == 0
