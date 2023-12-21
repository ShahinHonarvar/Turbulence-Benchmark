
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal_integer = int(binary_string, 2)
    # Check if the decimal integer is divisible by the 34th Fibonacci number
    fibonacci_number = 0
    for i in range(34):
        fibonacci_number = fibonacci_number + (fibonacci_number + 1)
    return decimal_integer % fibonacci_number == 0
