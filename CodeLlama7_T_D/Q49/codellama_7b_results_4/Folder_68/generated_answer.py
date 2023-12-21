
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to a decimal integer
    decimal_int = int(binary_string, 2)
    # Initialize variables for the Fibonacci sequence
    fib1 = 0
    fib2 = 1
    fib3 = 0
    # Loop through the digits of the decimal integer
    for digit in str(decimal_int):
        # Check if the current digit is a 1
        if digit == "1":
            # If it is, add the current Fibonacci number to the total
            fib3 += fib2
    # Return True if the total is divisible by 38
    return (fib3 % 38) == 0
