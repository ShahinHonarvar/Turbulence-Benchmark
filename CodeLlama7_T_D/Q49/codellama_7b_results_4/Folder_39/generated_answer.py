
def if_decimal_is_divisible(binary_representation):
    # Convert the binary representation string to an integer
    decimal_integer = int(binary_representation, 2)
    # Initialize a counter for the Fibonacci sequence
    fib_counter = 0
    # Initialize the first two numbers of the Fibonacci sequence
    fib1 = 0
    fib2 = 1

    while decimal_integer > 0:
        # Check if the current number is divisible by the 15th number in the Fibonacci sequence
        if decimal_integer % fib15 == 0:
            return True

        else:
            return False

         # Increment the counter for the Fibonacci sequence
         fib_counter += 1

        # Compute the next number in the Fibonacci sequence using the recurrence relation
        fib15 = fib1 + fib2

    return False
