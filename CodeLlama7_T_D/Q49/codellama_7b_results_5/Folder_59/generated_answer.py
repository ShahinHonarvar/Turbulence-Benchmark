
def if_decimal_is_divisible(binary_string):
    # Convert binary string to integer
    decimal_integer = int(binary_string, 2)
    # Find the 74th Fibonacci number
    fibonacci_numbers = [0, 1]
    for i in range(2, 74):
        fibonacci_numbers.append(fibonacci_numbers[i - 1] + fibonacci_numbers[i - 2])
    # Check if decimal integer is divisible by the 74th Fibonacci number
    if decimal_integer % fibonacci_numbers[73] == 0:
        return True

    else:

        return False
