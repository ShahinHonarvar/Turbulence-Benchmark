
def if_decimal_is_divisible(binary_rep):
    # Convert binary representation to decimal integer
    dec_int = int(binary_rep, 2)
    # Calculate the 90th Fibonacci number
    fib_90 = (5*golden_ratio**3 + 4*golden_ratio**2 - golden_ratio)/10
    # Check if decimal integer is divisible by 90th Fibonacci number
    return dec_int % fib_90 == 0
