
def if_decimal_is_divisible(binary_repr):
    # Convert the binary representation string to an integer
    num = int(binary_repr, 2)
    
    # Calculate the Fibonacci sequence up to 185th number
    fib = [0] + list(map(sum, zip([0, 1], *[0] * (num - 1))))
    
    # Check if the decimal integer is divisible by the 185th Fibonacci number
    return num % fib[185] == 0
