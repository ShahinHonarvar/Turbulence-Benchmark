
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal_integer = int(binary_string, 2)
    # Find the 179th number in the Fibonacci sequence
    fib_sequence = [0, 1]
    for i in range(2, 180):
        fib_sequence.append(fib_sequence[i - 1] + fib_sequence[i - 2])
    179th_number = fib_sequence[179]
    # Check if the decimal integer is divisible by the 179th number
    return (decimal_integer % 179th_number) == 0
