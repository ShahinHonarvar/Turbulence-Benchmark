
def if_decimal_is_divisible(binary_str):
    # Convert the binary string to an integer
    num = int(binary_str, 2)
    # Find the position of the most significant bit
    msb_pos = len(binary_str) - 1
    # Initialize the Fibonacci sequence with the first two numbers
    fib = [0, 1]
    # Loop through the positions of the bits in the binary string
    for i in range(msb_pos):
        # If the bit at the current position is set to 1, add the corresponding Fibonacci number to the total
        if binary_str[i] == "1":
            num += fib[i % len(fib)]
    # Return True if the decimal integer is divisible by the 27th Fibonacci number, otherwise False
    return num % fib[-1] == 0
