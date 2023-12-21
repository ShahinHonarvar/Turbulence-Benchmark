
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to a decimal integer
    decimal_int = int(binary_string, 2)
    # Initialize variables for the Fibonacci sequence
    prev1, prev2 = 0, 1
    # Iterate through the Fibonacci sequence until we reach the 180th number
    while True:
        next_num = prev1 + prev2
        if next_num == 180:
            break
        prev1, prev2 = prev2, next_num
    # Check if the decimal integer is divisible by the 180th Fibonacci number
    return decimal_int % next_num == 0
