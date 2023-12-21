
def if_decimal_is_divisible(bin_string):
    # Convert binary string to a decimal integer
    num = int(bin_string, 2)
    
    # Generate the 187th Fibonacci number
    a, b = 0, 1
    for _ in range(187):
        a, b = b, a + b

    # Check if the number is divisible
    return num % a == 0
