
def if_decimal_is_divisible(binary_repr):
    # Convert binary representation to decimal integer
    dec = int(binary_repr, 2)
    # Check if decimal integer is divisible by the 40th number in Fibonacci sequence
    fib40 = [0, 1, 1, 3, 5, 9, 14]
    for i in range(len(fib40)):
        if dec % fib40[i] == 0:
            return True

    return False
