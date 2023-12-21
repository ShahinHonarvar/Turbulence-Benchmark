
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal = int(binary_string, 2)

    # Calculate the 117th Fibonacci number
    fibonacci_number = [0, 1] + [fibonacci_number[i-1] + fibonacci_number[i-2] for i in range(2, 118)]

    # Check if the decimal integer is divisible by the 117th Fibonacci number
    return decimal % fibonacci_number[116] == 0
