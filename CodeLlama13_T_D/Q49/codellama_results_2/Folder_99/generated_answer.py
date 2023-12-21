
def if_decimal_is_divisible(binary_str):
    # Convert the binary representation string to an integer
    num = int(binary_str, 2)
    
    # Calculate the 109th Fibonacci number
    fib = [0, 1] + [fib[i-1] + fib[i-2] for i in range(2, 108)]
    target = fib[108]
    
    # Check if the decimal integer is divisible by the target number
    return num % target == 0
