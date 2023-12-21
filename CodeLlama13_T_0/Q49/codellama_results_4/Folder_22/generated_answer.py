
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal = int(binary_string, 2)
    
    # Calculate the Fibonacci sequence up to 20
    fibonacci = [0] + [1] + [sum(fibonacci[i-1:i+1]) for i in range(2, 20)]
    
    # Check if the decimal is divisible by any of the numbers in the Fibonacci sequence
    for num in fibonacci:
        if decimal % num == 0:
            return True
    
    # If none of the numbers in the Fibonacci sequence divide the decimal, return False
    return False
