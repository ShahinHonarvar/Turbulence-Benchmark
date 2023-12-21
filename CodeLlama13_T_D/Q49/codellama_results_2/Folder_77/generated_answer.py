
def if_decimal_is_divisible(binary_repr):
    # Convert binary representation string to integer
    num = int(binary_repr, 2)

    # Calculate the Fibonacci sequence up to the 110th number
    fib_seq = [0] + [n for n in range(num+1)]

    # Check if the decimal integer is divisible by the 110th number
    return num % fib_seq[110] == 0
