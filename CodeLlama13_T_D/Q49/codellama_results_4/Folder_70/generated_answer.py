
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal = int(binary_string, 2)
    
    # Initialize a variable to keep track of the Fibonacci sequence
    fibonacci = [0]
    
    # Calculate the Fibonacci sequence up to the 137th number
    for i in range(1, 138):
        fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])
    
    # Check if the decimal integer is divisible by the 137th Fibonacci number
    return decimal % fibonacci[136] == 0
