
def if_decimal_is_divisible(binary_repr):
    # Convert binary representation string to integer
    num = int(binary_repr, 2)
    # Calculate the Fibonacci sequence up to the 154th number
    fib = [0] + [0, 1]
    for i in range(3, 154):
        fib.append(fib[i-1] + fib[i-2])
    # Check if the decimal integer is divisible by the 154th Fibonacci number
    return num % fib[154] == 0
