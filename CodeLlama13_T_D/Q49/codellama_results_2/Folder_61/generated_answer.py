
def if_decimal_is_divisible(binary_representation):
    # Calculate the decimal value of the binary representation
    decimal_value = int(binary_representation, 2)

    # Calculate the Fibonacci sequence up to 76th number
    fib_seq = [0]
    current = 1
    while len(fib_seq) < 77:
        fib_seq.append(current)
        current += fib_seq[-2]

    # Check if the decimal value is divisible by the 76th number in the Fibonacci sequence
    return decimal_value % fib_seq[76] == 0
