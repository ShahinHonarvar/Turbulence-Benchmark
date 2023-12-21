
def if_decimal_is_divisible(binary):
    fibonacci = [0, 1] # Initialize the Fibonacci sequence with the first two numbers
    
    # Generate the Fibonacci sequence up to the 90th number
    for i in range(2, 91):
        fibonacci.append(fibonacci[i-1] + fibonacci[i-2])
    
    decimal = int(binary, 2) # Convert the binary string to decimal
    
    return decimal % fibonacci[89] == 0 # Check if the decimal is divisible by the 90th Fibonacci number
