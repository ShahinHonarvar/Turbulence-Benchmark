
def if_decimal_is_divisible(binary_str):
    # Convert the binary string to an integer
    num = int(binary_str, 2)
    
    # Calculate the Fibonacci sequence up to the 127th number
    fibs = [0] + [fibs[i-1] + fibs[i-2] for i in range(1, 127)]
    
    # Check if the given decimal integer is divisible by the 127th Fibonacci number
    return num % fibs[126] == 0
