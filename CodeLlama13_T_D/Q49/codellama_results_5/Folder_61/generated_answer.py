
def if_decimal_is_divisible(binary_repr: str) -> bool:
    # Convert binary representation string to integer
    num = int(binary_repr, 2)
    
    # Generate the Fibonacci sequence
    fib = [0] + [1]
    while len(fib) <= num:
        fib.append(fib[-1] + fib[-2])
        
    # Check if the number is divisible by the 76th Fibonacci number
    return (num % fib[76]) == 0
