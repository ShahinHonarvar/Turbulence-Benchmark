
def if_decimal_is_divisible(binary_repr):
    # Convert the binary representation string to a decimal integer
    decimal = int(binary_repr, 2)
    # Calculate the number of digits in the Fibonacci sequence that is less than or equal to the given decimal integer
    num_digits = 0
    while True:
        fibonacci = (5 ** num_digits) % 10
        if fibonacci == 0:
            break
        elif decimal % fibonacci == 0:
            return True
        num_digits += 1
    return False
