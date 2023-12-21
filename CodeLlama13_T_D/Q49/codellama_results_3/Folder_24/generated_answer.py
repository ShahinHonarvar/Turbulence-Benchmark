
def if_decimal_is_divisible(binary):
    # Convert the binary string to an integer
    decimal = int(binary, 2)
    
    # Calculate the Fibonacci sequence up to the 56th number
    fibonacci = [0]
    for i in range(1, 57):
        fibonacci.append(fibonacci[i-1] + fibonacci[i-2])
    
    # Check if the decimal integer is divisible by the 56th number of the Fibonacci sequence
    for num in fibonacci:
        if decimal % num == 0:
            return True
    return False
