
def if_decimal_is_divisible(binary_str):
    # Convert binary string to integer
    decimal = int(binary_str, 2)
    
    # Initialize Fibonacci sequence and 45th number occurrence counter
    fib = [0, 1]
    count = 0
    
    # Iterate through Fibonacci sequence until 45th number is found
    while count < 45:
        fib.append(fib[-1] + fib[-2])
        if fib[-1] % 2 == 0:
            count += 1
    
    # Return true if decimal integer is divisible by 45th Fibonacci number, else false
    return (decimal % fib[44]) == 0
