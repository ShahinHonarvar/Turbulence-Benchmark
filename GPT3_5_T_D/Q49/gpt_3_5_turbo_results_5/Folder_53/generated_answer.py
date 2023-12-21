
def if_decimal_is_divisible(binary):
    # Generate Fibonacci sequence up to the 64th number
    fib_sequence = [0, 1]
    for i in range(2, 65):
        fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])

    # Convert binary to decimal
    decimal = int(binary, 2)

    # Check if decimal is divisible by the 64th Fibonacci number
    if decimal % fib_sequence[63] == 0:
        return True
    else:
        return False
