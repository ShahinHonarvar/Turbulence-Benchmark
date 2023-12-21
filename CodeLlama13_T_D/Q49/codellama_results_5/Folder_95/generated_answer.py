
def if_decimal_is_divisible(binary_repr):
    # Convert the binary representation string to an integer
    num = int(binary_repr, 2)
    
    # Calculate the Fibonacci sequence up to the 168th number
    fibs = [0] + [fibs[-1] + fibs[-2] for _ in range(167)]
    
    # Check if the decimal integer is divisible by the 168th Fibonacci number
    return num % fibs[168] == 0
