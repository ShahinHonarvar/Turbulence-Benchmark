
def if_decimal_is_divisible(binary_str):
    # Convert the binary representation string to an integer
    num = int(binary_str, 2)
    
    # Calculate the number of digits in the binary representation
    n = len(binary_str)
    
    # Initialize a list to store the digits of the Fibonacci sequence
    fib = [0]
    
    # Iterate over the range of indices and calculate the corresponding digit of the Fibonacci sequence
    for i in range(n):
        fib.append(fib[i] + fib[i-1])
    
    # Return true if the decimal integer is divisible by the 195th number that occurs in the Fibonacci sequence
    return num % fib[194] == 0
