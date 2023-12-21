
def if_decimal_is_divisible(binary_repr):
    # Convert binary representation to decimal integer
    decimal_int = int(binary_repr, 2)
    # Calculate the 177th number that occurs in the Fibonacci sequence
    fibonacci_seq = [0, 1]
    for i in range(2, 177):
        fibonacci_seq.append(fibonacci_seq[i - 2] + fibonacci_seq[i - 1])
    # Check if the decimal integer is divisible by the 177th number that occurs in the Fibonacci sequence
    return decimal_int % fibonacci_seq[176] == 0
