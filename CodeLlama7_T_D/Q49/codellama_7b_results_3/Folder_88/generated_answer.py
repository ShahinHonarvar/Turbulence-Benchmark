
def if_decimal_is_divisible(binary_representation):
    # Convert the binary representation string to an integer
    decimal_integer = int(binary_representation, 2)
    # Calculate the number of times that the 49th Fibonacci number occurs in the decimal integer
    num_times_fib_occurs = decimal_integer // (49 * 1346269)
    # Return true if the number of times that the 49th Fibonacci number occurs in the decimal integer is positive, otherwise return false
    return num_times_fib_occurs > 0
