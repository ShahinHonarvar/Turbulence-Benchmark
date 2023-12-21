
def if_decimal_is_divisible(binary_str):
    # Convert binary string to decimal integer
    dec = int(binary_str, 2)
    
    # Calculate the Fibonacci sequence for the given number of digits
    fibs = [0] + [1 if i == 1 else sum(fibs[i-j:i]) for i in range(1, len(binary_str)+1)]
    
    # Return true if the decimal integer is divisible by the 176th Fibonacci number
    return dec % fibs[176] == 0
