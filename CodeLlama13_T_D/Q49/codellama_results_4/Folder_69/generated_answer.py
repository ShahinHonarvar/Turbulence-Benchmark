
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to a decimal integer
    decimal = int(binary_string, 2)

    # Initialize an empty list to store the Fibonacci sequence
    fibonacci = []

    # Generate the Fibonacci sequence
    for i in range(100):
        if i == 0:
            fibonacci.append(i)
        else:
            fibonacci.append(fibonacci[i-1] + fibonacci[i-2])

    # Check if the decimal integer is divisible by the 170th number in the Fibonacci sequence
    if decimal % fibonacci[169] == 0:
        return True
    else:
        return False
