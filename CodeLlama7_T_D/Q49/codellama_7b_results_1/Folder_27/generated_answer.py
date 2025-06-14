
def if_decimal_is_divisible(binary_representation):
    # Convert binary representation to decimal
    decimal = int(binary_representation, 2)
    # Initialize Fibonacci sequence with first two numbers
    fib = [0, 1]
    # Calculate remaining Fibonacci numbers up to the 87th number
    for i in range(2, 87):
        fib.append(fib[i - 1] + fib[i - 2])
    # Check if decimal integer is divisible by 87th Fibonacci number
    if decimal % fib[86] == 0:
        return True

    else:

        return False
