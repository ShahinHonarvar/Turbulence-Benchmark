
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal = int(binary_string, 2)
    
    # Calculate the 166th Fibonacci number
    fibonacci = [0] * (167 - 1)
    for i in range(len(fibonacci)):
        if i <= 1:
            fibonacci[i] = i
        else:
            fibonacci[i] = fibonacci[i-2] + fibonacci[i-1]
    
    # Check if the decimal integer is divisible by the 166th Fibonacci number
    return (decimal % fibonacci[166]) == 0
