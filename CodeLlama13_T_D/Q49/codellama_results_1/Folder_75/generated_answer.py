
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to a decimal number
    decimal = int(binary_string, 2)

    # Calculate the 189th Fibonacci number
    fib189 = (((1 + 5 ** 0.5) / 2) ** 189 - ((1 - 5 ** 0.5) / 2) ** 189) / 5 ** 0.5

    # Check if the decimal number is divisible by the 189th Fibonacci number
    return decimal % fib189 == 0
