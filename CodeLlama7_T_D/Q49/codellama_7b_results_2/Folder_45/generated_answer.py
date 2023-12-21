
def if_decimal_is_divisible(binary_string):
    # Convert binary string to decimal integer
    decimal_integer = int(binary_string, 2)
    # Initialize Fibonacci sequence with first two numbers
    fibonacci = [0, 1]
    # Calculate Fibonacci sequence up to 28th number
    while len(fibonacci) <= 28:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    # Check if decimal integer is divisible by 28th Fibonacci number
    return decimal_integer % fibonacci[27] == 0
