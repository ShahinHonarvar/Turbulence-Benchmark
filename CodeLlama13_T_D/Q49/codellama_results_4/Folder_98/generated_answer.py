
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to a decimal integer
    dec_int = int(binary_string, 2)

    # Calculate the Fibonacci sequence up to 14 terms
    fib_seq = [0, 1]
    for i in range(2, 14):
        fib_seq.append((fib_seq[i - 2] + fib_seq[i - 1]) % (10 ** 9 + 7))

    # Check if the decimal integer is divisible by any of the Fibonacci numbers
    for i in range(1, 14):
        if dec_int % fib_seq[i] == 0:
            return True

    # If no match was found, return False
    return False
