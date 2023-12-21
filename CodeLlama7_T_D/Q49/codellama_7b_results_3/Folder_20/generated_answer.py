
def if_decimal_is_divisible(binary_str):
    # Convert the binary string to an integer
    num = int(binary_str, 2)
    # Calculate the 100th number in the Fibonacci sequence
    fib100 = (5**0.5 + 1) / 2
    # Check if the decimal integer is divisible by the 100th Fibonacci number
    return num % fib100 == 0
