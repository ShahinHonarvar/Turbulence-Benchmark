
def if_decimal_is_divisible(binary):
    # Convert binary representation string to decimal integer
    n = int(binary, 2)
    
    # Calculate the Fibonacci sequence until the 60th number is reached
    fibonacci = [0, 1]
    while len(fibonacci) < 60:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    
    # Check if n is divisible by the 60th number in Fibonacci sequence
    return n % fibonacci[59] == 0
