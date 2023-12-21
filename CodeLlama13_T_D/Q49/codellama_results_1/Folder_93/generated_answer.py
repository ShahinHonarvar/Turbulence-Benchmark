
def if_decimal_is_divisible(binary_repr):
    # Convert binary representation string to integer
    decimal = int(binary_repr, 2)

    # Calculate the Fibonacci sequence until the 59th number is reached
    fib = [0, 1]
    for i in range(58):
        fib.append(fib[i] + fib[i+1])
    
    # Check if the decimal integer is divisible by the 59th Fibonacci number
    return decimal % fib[-1] == 0
