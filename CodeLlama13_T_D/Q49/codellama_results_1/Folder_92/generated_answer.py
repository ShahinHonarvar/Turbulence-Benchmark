
def if_decimal_is_divisible(binary_representation):
    # Convert the binary representation string to an integer
    decimal = int(binary_representation, 2)

    # Calculate the 7th number that occurs in the Fibonacci sequence
    fib_7 = 13

    # Check if the decimal is divisible by the 7th number of the Fibonacci sequence
    if decimal % fib_7 == 0:
        return True
    else:
        return False
