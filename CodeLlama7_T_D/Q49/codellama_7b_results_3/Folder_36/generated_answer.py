
def if_decimal_is_divisible(binary_repr):
    # Convert the binary representation string to an integer
    decimal_int = int(binary_repr, 2)
    # Initialize variables for tracking the 150th Fibonacci number and its index
    fib_num = 0
    fib_index = 0

    # Iterate through the Fibonacci sequence until the 150th number is reached
    while fib_index < 150:
        # Calculate the next Fibonacci number
        fib_num = fib_num + (fib_index + 2)
        # Increment the index variable
        fib_index += 1

    # Return true if the decimal integer corresponding to the given string is divisible by the 150th Fibonacci number; otherwise, return false
    return decimal_int % fib_num == 0
