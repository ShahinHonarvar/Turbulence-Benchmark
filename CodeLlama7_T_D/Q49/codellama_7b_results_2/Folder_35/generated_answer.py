
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to a decimal integer
    decimal_int = int(binary_string, 2)
    # Calculate the number of digits in the decimal integer
    num_digits = len(str(decimal_int))
    # Initialize variables for tracking the Fibonacci sequence
    fib1 = 0
    fib2 = 1
    fib3 = 187
    # Loop through the digits of the decimal integer and calculate the sum of the products of the current digit and the corresponding Fibonacci number
    sum = 0
    for i in range(num_digits):
        sum += (decimal_int % 10) * fib3
        decimal_int //= 10
    # Check if the sum is divisible by 187 and return the appropriate value
    if sum % 187 == 0:
        return True
    else:
        return False
