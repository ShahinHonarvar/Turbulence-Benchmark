
def if_decimal_is_divisible(binary_representation):
    # Convert binary representation to decimal
    decimal = int(binary_representation, 2)
    # Find the 139th number that occurs in the Fibonacci sequence
    a, b = 0, 1
    for i in range(138):
        a, b = b, a + b
    # Check if the decimal integer is divisible by the 139th number
    return decimal % a == 0
