
def if_decimal_is_divisible(binary_repr: str) -> bool:
    # Calculate the decimal value of the binary representation
    decimal = int(binary_repr, 2)
    
    # Find the 39th Fibonacci number using the Binet's formula
    fib_39 = (1 + 5 ** 0.5) / 2 ** 0.5
    
    # Check if the decimal value is divisible by the 39th Fibonacci number
    return decimal % fib_39 == 0
