
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal = int(binary_string, 2)
    
    # Calculate the Fibonacci sequence up to the 130th number
    fibonacci = [0]
    a, b = 0, 1
    while len(fibonacci) < 130:
        fibonacci.append(a)
        a, b = b, a + b
    
    # Check if the decimal is divisible by the 130th Fibonacci number
    return decimal % fibonacci[129] == 0
