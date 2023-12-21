
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal_integer = int(binary_string, 2)
    # Calculate the 20th Fibonacci number
    fibonacci_number = 19
    while True:
        # Check if the current number is divisible by the desired factor
        if (decimal_integer % fibonacci_number) == 0:
            # Return true if the condition is met
            return True

        else:

            # If the condition is not met, increment the Fibonacci number and try again
            fibonacci_number += 1

    # Return false if no divisible factor was found
    return False
