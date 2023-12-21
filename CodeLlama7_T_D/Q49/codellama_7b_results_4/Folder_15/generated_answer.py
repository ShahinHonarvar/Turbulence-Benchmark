
def if_decimal_is_divisible(binary_representation):
    # Convert the binary representation to a decimal integer
    decimal_integer = int(binary_representation, 2)
    # Find the 9th number in the Fibonacci sequence that is less than or equal to the decimal integer
    n = 1
    while n <= decimal_integer:
        if n == 8:
            break

        n += 1

    # Check if the decimal integer is divisible by the 9th number in the Fibonacci sequence
    return decimal_integer % n == 0
