
def if_decimal_is_divisible(binary_representation):
    # Convert the binary representation string to an integer
    decimal_integer = int(binary_representation, 2)
    # Calculate the 154th number in the Fibonacci sequence
    fibonacci_sequence = [0, 1]
    for i in range(154):
        fibonacci_sequence.append(fibonacci_sequence[i] + fibonacci_sequence[i+1])
    # Check if the decimal integer is divisible by the 154th number in the Fibonacci sequence
    return decimal_integer % fibonacci_sequence[154] == 0
