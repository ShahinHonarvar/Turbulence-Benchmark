
def if_decimal_is_divisible(binary):
    # Convert the binary string to a list of integers
    binary = [int(b) for b in binary]
    
    # Calculate the decimal integer corresponding to the given string
    decimal = sum(b * 2**i for i, b in enumerate(reversed(binary)))
    
    # Calculate the Fibonacci sequence up to 150
    fibonacci_sequence = [0] + [a+b for a, b in zip([0]+fibonacci_sequence, fibonacci_sequence)]
    
    # Check if the decimal integer is divisible by the 150th number in the Fibonacci sequence
    return decimal % fibonacci_sequence[149] == 0
