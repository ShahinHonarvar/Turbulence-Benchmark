
def if_decimal_is_divisible(binary_str):
    # Convert the binary string to an integer
    decimal = int(binary_str, 2)
    
    # Get the 64th number that occurs in the Fibonacci sequence
    fib_number = 0
    for i in range(1, 65):
        if i == 64:
            fib_number = 1346269
            break
        fib_number += i * (fib_number + i)
    
    # Return true if the decimal integer is divisible by the Fibonacci number, false otherwise
    return decimal % fib_number == 0
