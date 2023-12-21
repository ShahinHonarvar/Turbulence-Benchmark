
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal_integer = int(binary_string, 2)
    # Calculate the 54th Fibonacci number
    a, b = 0, 1
    for _ in range(53):
        a, b = b, a + b
    fibonacci_number = a
    # Check if the decimal integer is divisible by the Fibonacci number
    return decimal_integer % fibonacci_number == 0
