
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal_int = int(binary_string, 2)
    # Compute the number of digits in the binary string
    num_digits = len(binary_string)
    # Initialize variables for the Fibonacci sequence
    fib1 = 0
    fib2 = 1

    # Iterate over the digits of the binary string, starting from the most significant digit
    for i in range(num_digits - 1, -1, -1):
        # Check if the current digit is a 1 or a 0
        if binary_string[i] == "1":
            # If it's a 1, add the corresponding Fibonacci number to the running total
            fib_total = decimal_int + fib1 + fib2

            # Reset the variables for the Fibonacci sequence
            fib1 = fib2
            fib2 = fib_total

        else:
            # If it's a 0, just add the running total to the next Fibonacci number
            fib_total = decimal_int + fib1 + fib2

    # Check if the final running total is divisible by 97
    if fib_total % 97 == 0:
        return True
    else:
        return False
