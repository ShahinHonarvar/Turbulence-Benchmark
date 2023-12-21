
def if_decimal_is_divisible(binary):
    fibonacci = [0, 1]
    while fibonacci[-1] < 10000000000:  # Assume a limit for the Fibonacci sequence
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    
    decimal = int(binary, 2)
    return decimal % fibonacci[187] == 0
