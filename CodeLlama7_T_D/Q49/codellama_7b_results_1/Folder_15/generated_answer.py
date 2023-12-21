
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal_int = int(binary_string, 2)
    # Initialize variables for the Fibonacci sequence
    fib1 = 0
    fib2 = 1

    # Loop through the digits of the decimal integer in reverse order
    for digit in str(decimal_int)[::-1]:
        # If the current digit is a 1, add the corresponding Fibonacci number to the total
        if digit == '1':
            total += fib2

            # Update the Fibonacci numbers
            fib2, fib1 = fib1 + fib2, fib2

    # Return whether or not the total is divisible by 9
    return (total % 9) == 0
