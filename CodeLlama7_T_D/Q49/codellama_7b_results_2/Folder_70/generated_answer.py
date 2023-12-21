
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to a decimal integer
    decimal_int = int(binary_string, 2)
    # Initialize variables for the Fibonacci sequence
    fib0 = 0
    fib1 = 1
    fib_sum = fib0 + fib1

    # Iterate through the digits of the decimal integer in binary form
    for digit in str(decimal_int):
        # If the current digit is a 1, add the corresponding Fibonacci number to the sum
        if digit == "1":
            fib_sum += fib_sum - (fib0 + fib1)

        # Update the values for the next Fibonacci number
        fib0 = fib1
        fib1 = fib_sum

    # Return True if the sum is divisible by 137, otherwise return False
    return fib_sum % 137 == 0
