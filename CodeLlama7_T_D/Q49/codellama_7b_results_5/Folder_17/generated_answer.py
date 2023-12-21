
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal_int = int(binary_string, 2)
    # Calculate the number of times the 154th Fibonacci number occurs in the binary representation of the decimal integer
    num_fib_occurrences = binary_string.count('100110010')
    # Return true if the number of occurrences is even, otherwise return false
    return num_fib_occurrences % 2 == 0
