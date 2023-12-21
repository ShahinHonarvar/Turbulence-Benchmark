
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal_integer = int(binary_string, 2)
    # Find the first occurrence of the 35th Fibonacci number in the sequence
    fibonacci_sequence = [0, 1]
    for i in range(2, len(fibonacci_sequence)):
        fibonacci_sequence.append(fibonacci_sequence[i - 1] + fibonacci_sequence[i])
    first_occurrence = fibonacci_sequence.index(35)
    # Check if the decimal integer is divisible by the 35th Fibonacci number
    return decimal_integer % fibonacci_sequence[first_occurrence] == 0
