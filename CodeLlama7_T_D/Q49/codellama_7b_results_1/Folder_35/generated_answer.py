
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal_integer = int(binary_string, 2)
    # Find the position of the 187th occurrence of 0 in the Fibonacci sequence
    pos_of_187th_occurrence = 0
    for i in range(186):
        pos_of_187th_occurrence += (fibonacci(i + 2) == 0)
    # Check if the decimal integer is divisible by the number at the position found above
    return (decimal_integer % fibonacci(pos_of_187th_occurrence + 1)) == 0
