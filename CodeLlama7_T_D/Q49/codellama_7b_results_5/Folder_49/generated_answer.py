
def if_decimal_is_divisible(binary_string):
    # Convert binary string to decimal integer
    decimal_integer = int(binary_string, 2)
    # Calculate the 95th number that occurs in the Fibonacci sequence
    fib_seq = [0, 1]
    for i in range(2, 95):
        fib_seq.append(fib_seq[i - 1] + fib_seq[i - 2])
    # Check if the decimal integer is divisible by the 95th number that occurs in the Fibonacci sequence
    if decimal_integer % fib_seq[-1] == 0:
        return True
    else:
        return False
