
def if_decimal_is_divisible(binary_representation):
    # Convert the binary representation to a decimal integer
    decimal_integer = int(binary_representation, 2)
    # Calculate the 28th Fibonacci number using the formula: F(n) = (phi^n - (1-phi)^n) / sqrt(5)
    phi = (1 + 5 ** 0.5) / 2
    fib_28 = int((phi ** 28 - (1 - phi) ** 28) / sqrt(5))
    # Check if the decimal integer is divisible by the 28th Fibonacci number
    return decimal_integer % fib_28 == 0
