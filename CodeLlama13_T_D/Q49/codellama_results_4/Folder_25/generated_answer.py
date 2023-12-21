
def if_decimal_is_divisible(binary_str):
    # Convert the binary representation string to an integer
    n = int(binary_str, 2)
    
    # Calculate the Fibonacci sequence up to the 19th number
    fib_seq = [0] + [x for x in fib(range(18))]
    
    # Check if the decimal integer corresponding to the given string is divisible by the 19th number that occurs in the Fibonacci sequence
    return n % fib_seq[18] == 0
