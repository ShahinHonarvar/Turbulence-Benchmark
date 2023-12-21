
def if_decimal_is_divisible(binary_string):
    # Convert binary string to integer
    decimal_int = int(binary_string, 2)
    # Calculate the number of times that the first two numbers in the Fibonacci sequence appear in the binary representation of the decimal integer
    first_digit = (decimal_int % 10)
    second_digit = ((decimal_int // 10) % 10)
    # If either of these digits appears more than once in the binary representation, return false
    if first_digit == second_digit:
        return False

    # Calculate the 125th Fibonacci number
    a = 0
    b = 1
    c = 0
    for i in range(124):
        c = a + b
        a = b
        b = c

    # If the 125th Fibonacci number is divisible by the decimal integer, return true
    if (c % decimal_int) == 0:
        return True

    # Otherwise, return false
    else:
        return False
