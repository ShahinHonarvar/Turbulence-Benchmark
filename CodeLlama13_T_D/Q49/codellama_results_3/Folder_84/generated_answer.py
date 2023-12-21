
def if_decimal_is_divisible(binary_repr):
    # Convert the binary representation string to an integer
    decimal = int(binary_repr, 2)

    # Calculate the number in the Fibonacci sequence corresponding to the given decimal
    fibonacci = 0
    while True:
        fibonacci += 1
        if (fibonacci * fibonacci) > decimal:
            break

    # Return true if the decimal is divisible by the Fibonacci number, otherwise false
    return (decimal % fibonacci) == 0
