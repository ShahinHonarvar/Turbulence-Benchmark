
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal = int(binary_string, 2)

    # Get the 177th number in the Fibonacci sequence
    fib_177 = 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610

    # Check if the decimal number is divisible by the 177th Fibonacci number
    return decimal % fib_177[177] == 0
