
def if_decimal_is_divisible(binary_repr):
    # Extract the decimal integer from the binary representation string
    decimal_int = int(binary_repr, 2)
    # Calculate the Fibonacci sequence up to the 138th number
    fib_seq = [0, 1]
    for i in range(2, 138):
        fib_seq.append(fib_seq[i - 1] + fib_seq[i - 2])
    # Check if the decimal integer is divisible by any of the Fibonacci numbers
    for num in fib_seq:
        if decimal_int % num == 0:
            return True

    return False
