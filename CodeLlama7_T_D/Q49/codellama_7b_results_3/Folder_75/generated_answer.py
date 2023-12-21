
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to a decimal integer
    decimal_integer = int(binary_string, 2)
    # Calculate the Fibonacci sequence up to the 189th term
    fibonacci_sequence = [0, 1]
    for i in range(189):
        fibonacci_sequence.append(fibonacci_sequence[i] + fibonacci_sequence[i+1])
    # Check if the decimal integer is divisible by the 189th Fibonacci number
    return decimal_integer % fibonacci_sequence[188] == 0
