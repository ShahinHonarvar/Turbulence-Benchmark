
def if_decimal_is_divisible(binary_representation):
    # Convert binary representation string to an integer
    decimal = int(binary_representation, 2)
    
    # Calculate the 80th Fibonacci number using Binet's formula
    fib80 = (1 + 5**0.5) / 2 * 5**(80/2) - (1 - 5**0.5) / 2 * 5**((80-1)/2)
    
    # Return True if the decimal is divisible by the 80th Fibonacci number, False otherwise
    return decimal % int(fib80) == 0
