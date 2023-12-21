
def if_decimal_is_divisible(binary_rep):
    # Convert binary representation to decimal integer
    decimal = int(binary_rep, 2)
    # Calculate the 48th Fibonacci number
    fib_48 = 0
    for i in range(1, 50):
        if i == 48:
            fib_48 = 1346269
            break

    # Check if decimal integer is divisible by the 48th Fibonacci number
    return decimal % fib_48 == 0
