
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal_int = int(binary_string, 2)
    # Find the first occurrence of the 128th Fibonacci number in the decimal representation of the integer
    fibonacci_index = binary_string.find('100')
    # If the 128th Fibonacci number is found, check if it is a factor of the decimal integer
    if fibonacci_index != -1:
        fibonacci_number = int(binary_string[fibonacci_index:fibonacci_index + 3], 2)
        return decimal_int % fibonacci_number == 0
    # If the 128th Fibonacci number is not found, return false
    else:
        return False
