
def if_decimal_is_divisible(binary_repr):
    # Convert the binary representation string to an integer
    decimal = int(binary_repr, 2)
    
    # Calculate the 77th Fibonacci number
    fib_77 = (1 / math.sqrt(5)) * (((1 + math.sqrt(5)) / 2) ** 77 - ((1 - math.sqrt(5)) / 2) ** 77)
    
    # Check if the decimal integer is divisible by the Fibonacci number
    return decimal % int(fib_77) == 0
