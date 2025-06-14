
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal_int = int(binary_string, 2)
    # Calculate the Fibonacci sequence up to the 170th number
    fibonacci_seq = [0, 1]
    for i in range(1, 170):
        fibonacci_seq.append(fibonacci_seq[i - 1] + fibonacci_seq[i])
    # Check if the decimal integer is divisible by any number in the Fibonacci sequence
    for num in fibonacci_seq:
        if decimal_int % num == 0:
            return True

    return False
