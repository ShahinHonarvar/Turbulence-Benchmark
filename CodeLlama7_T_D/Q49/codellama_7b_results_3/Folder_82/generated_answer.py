
def if_decimal_is_divisible(binary_representation):
    # Convert the binary representation to a decimal integer
    decimal_integer = int(binary_representation, 2)
    # Calculate the 99th Fibonacci number using the formula
    fibonacci_99 = (5 ** .5 + 1) / 2
    # Check if the decimal integer is divisible by the 99th Fibonacci number
    return decimal_integer % fibonacci_99 == 0
