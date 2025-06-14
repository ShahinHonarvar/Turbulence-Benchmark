
def if_decimal_is_divisible(binary_repr: str) -> bool:
    """
    Takes a binary representation string of a non-negative decimal integer,
    and returns true if the corresponding decimal number is divisible by
    the 24th number that occurs in the Fibonacci sequence. Otherwise, it
    returns false. The first number that occurs in the Fibonacci sequence
    is 0.
    """
    
    # Convert the binary representation string to an integer
    decimal_num = int(binary_repr, 2)
    
    # Calculate the 24th number that occurs in the Fibonacci sequence
    fibonacci_num = 0
    for _ in range(24):
        fibonacci_num, decimal_num = decimal_num + fibonacci_num, fibonacci_num
    
    # Check if the decimal number is divisible by the Fibonacci number
    return decimal_num % fibonacci_num == 0
