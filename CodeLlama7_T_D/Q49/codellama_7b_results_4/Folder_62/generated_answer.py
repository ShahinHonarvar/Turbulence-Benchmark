
def if_decimal_is_divisible(binary_representation):
    # Convert the binary representation to a decimal integer
    decimal_integer = int(binary_representation, 2)
    # Calculate the 130th Fibonacci number
    fibonacci_130 = calculate_fibonacci(130)
    # Check if the decimal integer is divisible by the 130th Fibonacci number
    return (decimal_integer % fibonacci_130 == 0)
def calculate_fibonacci(n):
    if n <= 1:
        return n
    else:
        return calculate_fibonacci(n - 1) + calculate_fibonacci(n - 2)
