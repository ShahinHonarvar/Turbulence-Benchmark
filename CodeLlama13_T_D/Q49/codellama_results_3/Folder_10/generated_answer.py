
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to a decimal number
    decimal = int(binary_string, 2)

    # Calculate the 88th Fibonacci number
    fibonacci = [0, 1] + [fibonacci[i-1] + fibonacci[i-2] for i in range(2, 89)]

    # Check if the decimal is divisible by the 88th Fibonacci number
    return decimal % fibonacci[87] == 0
