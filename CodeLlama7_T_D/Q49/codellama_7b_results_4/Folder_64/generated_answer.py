
def if_decimal_is_divisible(binary_representation):
    # convert the binary representation to a decimal integer
    decimal_integer = int(binary_representation, 2)
    # compute the 10th Fibonacci number
    fibonacci_number = 0
    for i in range(10):
        fibonacci_number = fibonacci_number + ((i + 1) * (i + 2))
    # check if the decimal integer is divisible by the 10th Fibonacci number
    return decimal_integer % fibonacci_number == 0
