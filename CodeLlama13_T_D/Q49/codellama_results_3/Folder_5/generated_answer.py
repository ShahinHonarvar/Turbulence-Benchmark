
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to a decimal integer
    decimal = int(binary_string, 2)
    
    # Calculate the 85th Fibonacci number
    fibonacci_num = 0
    for i in range(85):
        fibonacci_num += fibonacci(i)
        
    # Check if the decimal integer is divisible by the Fibonacci number
    if decimal % fibonacci_num == 0:
        return True
    else:
        return False
    
# Function to calculate the Fibonacci number for a given index
def fibonacci(index):
    if index <= 1:
        return index
    else:
        return fibonacci(index - 1) + fibonacci(index - 2)
