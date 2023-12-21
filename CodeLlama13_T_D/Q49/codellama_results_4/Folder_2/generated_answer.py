
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to a decimal number
    decimal = int(binary_string, 2)
    
    # Get the 125th Fibonacci number using Binet's formula
    fib_125 = (((1+math.sqrt(5))/2)**125 - ((1-math.sqrt(5))/2)**125) / math.sqrt(5)
    
    # Check if the decimal number is divisible by the 125th Fibonacci number
    return (decimal % fib_125 == 0)
