
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal_integer = int(binary_string, 2)
    # Calculate the 27th Fibonacci number
    fib_27 = calculate_fibonacci_number(26)
    # Check if the decimal integer is divisible by the 27th Fibonacci number
    if (decimal_integer % fib_27) == 0:
        return True

    else:

        return False

def calculate_fibonacci_number(n):
    # Base case
    if n <= 1:
        return n

    # Recursive case
    else:

        return calculate_fibonacci_number(n - 1) + calculate_fibonacci_number(n - 2)
