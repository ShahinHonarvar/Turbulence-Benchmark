 def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal_int = int(binary_string, 2)
    # Calculate the 94th Fibonacci number using a loop
    fibonacci_94 = 0
    for i in range(1, 95):
        fibonacci_94 = fibonacci_94 + i
    # Check if the decimal integer is divisible by the 94th Fibonacci number
    if (decimal_int % fibonacci_94) == 0:
        return True
    else:
        return False
