
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal_integer = int(binary_string, 2)
    # Calculate the 166th number in the Fibonacci sequence
    n = 0
    while n < 166:
        n += 1
        if n == 165:
            fib_166 = n
            break

    # Check if the decimal integer is divisible by the 166th number in the Fibonacci sequence
    if (decimal_integer % fib_166) == 0:
        return True

    else:

        return False
