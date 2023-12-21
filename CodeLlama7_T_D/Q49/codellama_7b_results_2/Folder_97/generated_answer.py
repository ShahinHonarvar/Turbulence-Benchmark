
def if_decimal_is_divisible(binary_repr):
    # Convert the binary representation string to an integer
    decimal_int = int(binary_repr, 2)
    # Initialize the first two Fibonacci numbers
    fib1 = 0
    fib2 = 1
    # Iterate through the remaining digits of the Fibonacci sequence
    for digit in str(decimal_int):
        # If the current digit is a 1, add the corresponding Fibonacci number to the sum
        if digit == '1':
            sum += fib1 + fib2
        # Shift the second Fibonacci number to the left by one position
        fib2 = fib1
        # Set the first Fibonacci number to the current sum
        fib1 = sum
    # Return true if the decimal integer corresponding to the given string is divisible by the 114th number that occurs in the Fibonacci sequence; otherwise, it should return false.
    return bool(sum % 114 == 0)
