
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal = int(binary_string, 2)

    # Calculate the Fibonacci sequence up to 114th number
    fib = [0] * 115
    for i in range(114):
        fib[i+1] = fib[i] + fib[i-1]

    # Check if the decimal is divisible by 114th Fibonacci number
    return decimal % fib[114] == 0
