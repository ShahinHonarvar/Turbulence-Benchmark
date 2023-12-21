
def if_decimal_is_divisible(binary_representation):
    # Convert binary representation to integer
    decimal_integer = int(binary_representation, 2)
    # Calculate the 108th Fibonacci number
    a, b = 0, 1
    for _ in range(107):
        a, b = b, a + b
    # Check if the decimal integer is divisible by the 108th Fibonacci number
    return decimal_integer % a == 0
