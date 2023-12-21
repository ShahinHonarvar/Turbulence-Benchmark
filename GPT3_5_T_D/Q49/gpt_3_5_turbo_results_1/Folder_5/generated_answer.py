
def if_decimal_is_divisible(binary):
    fib_sequence = [0, 1]
    while fib_sequence[-1] < 10**18:  # 85th Fibonacci number is within range
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    
    decimal = 0
    for bit in binary:
        decimal = decimal * 2 + int(bit)
    
    return decimal % fib_sequence[84] == 0
