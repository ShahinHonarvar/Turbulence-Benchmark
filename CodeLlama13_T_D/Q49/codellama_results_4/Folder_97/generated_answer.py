
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to a decimal integer
    num = int(binary_string, 2)

    # Calculate the Fibonacci sequence up to 114th number
    fib_seq = [0] + list(map(lambda x: sum(x), zip(*[[0, 1]] * (len(str(num)) - 1))))

    # Check if the decimal integer is divisible by the 114th Fibonacci number
    return num % fib_seq[114] == 0
