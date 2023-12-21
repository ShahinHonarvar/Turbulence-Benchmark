
def if_decimal_is_divisible(binary_repr):
    # Convert the binary representation string to an integer
    num = int(binary_repr, 2)
    # Calculate the 127th number in the Fibonacci sequence
    fib_num = (((1+5**0.5)/2)**127 - (1-5**0.5)/(2*5**0.5))/5**0.5
    # Check if the decimal integer is divisible by the 127th number in the Fibonacci sequence
    return num % fib_num == 0
