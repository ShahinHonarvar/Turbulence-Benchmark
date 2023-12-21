
def if_decimal_is_divisible(binary_repr):
    # Convert the binary representation string to an integer
    num = int(binary_repr, 2)
    
    # Calculate the 6th Fibonacci number using Binet's formula
    fib6 = (1 / sqrt(5)) * ((1 + sqrt(5)) ** num - (1 - sqrt(5)) ** num)
    
    # Check if the decimal integer is divisible by the 6th Fibonacci number
    return num % int(fib6) == 0
