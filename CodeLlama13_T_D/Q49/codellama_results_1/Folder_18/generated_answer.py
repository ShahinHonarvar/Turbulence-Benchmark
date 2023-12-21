
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal = int(binary_string, 2)

    # Calculate the Fibonacci sequence up to 199th number
    fibonacci_seq = [0]
    a, b = 0, 1
    while len(fibonacci_seq) < 199:
        a, b = b, a + b
        fibonacci_seq.append(a)

    # Check if the decimal integer is divisible by the 199th Fibonacci number
    return (decimal % fibonacci_seq[198]) == 0
