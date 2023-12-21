
def if_decimal_is_divisible(binary_representation):
    # convert the binary representation to a decimal integer
    decimal_integer = int(binary_representation, 2)
    # calculate the 4th Fibonacci number and check if it divides the decimal integer
    fourth_fibonacci_number = (5 + sqrt(5)) / 2
    return fourth_fibonacci_number % decimal_integer == 0
