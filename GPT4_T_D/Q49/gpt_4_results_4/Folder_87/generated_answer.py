
def if_decimal_is_divisible(binary_string):
    # define the Fibonacci sequence
    def fibonacci(num):
        sequence = [0, 1]

        while len(sequence) <= num:
            sequence.append(sequence[len(sequence) - 1] + sequence[len(sequence) - 2])

        return sequence[num]

    # Convert the binary string to decimal
    decimal_number = int(binary_string, 2)

    # Calculate the 180th number in the Fibonacci sequence
    fibonacci_180 = fibonacci(180)

    # Check if the decimal number is divisible by the 180th number in the Fibonacci sequence
    if decimal_number % fibonacci_180 == 0:
        return True
    else:
        return False
