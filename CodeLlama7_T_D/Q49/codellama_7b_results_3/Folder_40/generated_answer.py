
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal_integer = int(binary_string, 2)
    # Calculate the number of digits in the integer
    num_digits = len(str(decimal_integer))
    # Initialize variables for the Fibonacci sequence
    fib1 = 0
    fib2 = 1
    fib3 = 0
    # Iterate over the digits of the integer, starting from the most significant digit
    for i in range(num_digits):
        # Calculate the current digit in the Fibonacci sequence based on the previous two digits
        fib3 = fib1 + fib2
        fib1 = fib2
        fib2 = fib3
        # Check if the current digit is divisible by 4
        if decimal_integer % 4 == 0:
            # If so, return true
            return True

    # If no digits are divisible by 4, return false
    return False
