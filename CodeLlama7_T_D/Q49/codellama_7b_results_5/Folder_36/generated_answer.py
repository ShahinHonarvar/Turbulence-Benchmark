 def if_decimal_is_divisible(binary_repr):
    # Convert the binary representation string to an integer
    decimal_int = int(binary_repr, 2)
    # Initialize variables for the Fibonacci sequence
    a = 0
    b = 1
    # Loop through the digits of the decimal integer and check if they are divisible by the corresponding number in the Fibonacci sequence
    for digit in str(decimal_int):
        if int(digit) % a == 0:
            return True

    return False
