
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal_integer = int(binary_string, 2)
    # Initialize a list to store the Fibonacci numbers
    fibonacci_numbers = [0, 1]
    # Generate the Fibonacci sequence up to the 170th number
    for i in range(169):
        fibonacci_numbers.append(fibonacci_numbers[i] + fibonacci_numbers[i+1])
    # Check if the decimal integer is divisible by any of the Fibonacci numbers
    for fibonacci_number in fibonacci_numbers:
        if decimal_integer % fibonacci_number == 0:
            return True

    # If none of the Fibonacci numbers divide the decimal integer, then return False

    return False
