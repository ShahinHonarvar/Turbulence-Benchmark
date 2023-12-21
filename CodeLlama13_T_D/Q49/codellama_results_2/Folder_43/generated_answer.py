
def if_decimal_is_divisible(binary):
    # Convert the binary representation string to a list of integers
    binary = [int(b) for b in binary[::-1]]
    
    # Calculate the decimal integer corresponding to the given string
    decimal = sum([2**i * binary[i] for i in range(len(binary))])
    
    # Find the 77th number that occurs in the Fibonacci sequence
    fib = [0, 1]
    while len(fib) <= 77:
        fib.append(fib[-2] + fib[-1])
    fib_77 = fib[77]
    
    # Check if the decimal integer is divisible by the 77th number that occurs in the Fibonacci sequence
    return decimal % fib_77 == 0
