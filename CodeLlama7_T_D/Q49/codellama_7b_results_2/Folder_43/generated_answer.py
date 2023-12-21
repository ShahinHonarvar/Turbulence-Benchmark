
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal_int = int(binary_string, 2)
    # Initialize variables for the Fibonacci sequence
    a = 0
    b = 1

    # Loop through the digits of the decimal integer
    for digit in str(decimal_int):
        # If the current digit is a 1, add the corresponding Fibonacci number to the sum
        if digit == "1":
            sum += a
            sum += b

        # Update the values for the next Fibonacci number
        c = a + b
        a = b
        b = c

    # Return True if the decimal integer is divisible by the 77th Fibonacci number, otherwise return False
    if sum % (a + b) == 0:
        return True
    else:
        return False
