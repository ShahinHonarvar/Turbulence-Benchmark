
def if_decimal_is_divisible(binary_representation):
    # Convert the binary representation string to a decimal integer
    decimal_integer = int(binary_representation, 2)
    # Initialize variables for the Fibonacci sequence
    fib1 = 0
    fib2 = 1

    # Check if the decimal integer is divisible by the 64th number in the Fibonacci sequence
    for i in range(63):
        fib_sum = fib1 + fib2
        fib1 = fib2
        fib2 = fib_sum

    return decimal_integer % fib2 == 0
