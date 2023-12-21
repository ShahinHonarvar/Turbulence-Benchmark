
def if_decimal_is_divisible(binary_repr):
    # Convert binary representation to decimal integer
    decimal_int = int(binary_repr, 2)
    # Calculate the 119th Fibonacci number
    fib_118 = 0
    fib_119 = 1
    for i in range(118):
        temp = fib_119
        fib_119 = fib_118 + fib_119
        fib_118 = temp
    # Check if the decimal integer is divisible by the 119th Fibonacci number
    return decimal_int % fib_119 == 0
