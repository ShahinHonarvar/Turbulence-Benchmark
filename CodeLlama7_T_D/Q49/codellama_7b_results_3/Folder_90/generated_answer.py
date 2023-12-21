
def if_decimal_is_divisible(binary_representation):
    # Convert binary representation to decimal
    decimal = int(binary_representation, 2)
    # Initialize Fibonacci sequence with first two numbers
    fibonacci = [0, 1]
    # Compute Fibonacci sequence up to the 177th number
    for i in range(176):
        fibonacci.append(fibonacci[i] + fibonacci[i+1])
    # Check if decimal is divisible by 177th Fibonacci number
    return decimal % fibonacci[176] == 0
