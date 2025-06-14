
def if_decimal_is_divisible(binary_string):
    # Convert binary string to integer
    decimal_int = int(binary_string, 2)
    # Calculate the 87th Fibonacci number
    fib_87 = calculate_fibonacci_number(87)
    # Check if the decimal integer is divisible by the 87th Fibonacci number
    if decimal_int % fib_87 == 0:
        return True
    else:
        return False

def calculate_fibonacci_number(n):
    # Initialize variables
    a = 0
    b = 1

    # Calculate the nth Fibonacci number using Binet's formula
    for i in range(n - 2):
        c = a + b
        a = b
        b = c

    return b
