
def if_decimal_is_divisible(binary_repr):
    # Convert binary representation to decimal integer
    decimal = int(binary_repr, 2)
    # Initialize Fibonacci sequence with first two numbers
    fib = [0, 1]
    # Calculate the 84th number in the Fibonacci sequence
    for i in range(84):
        fib.append(fib[-1] + fib[-2])
    # Check if decimal integer is divisible by 84th number in Fibonacci sequence
    return decimal % fib[83] == 0
