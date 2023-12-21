
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def if_decimal_is_divisible(binary):
    decimal = 0
    for i in range(len(binary)):
        if binary[i] == '1':
            decimal += fibonacci(len(binary) - i - 1)
        
    fifteenth_fibonacci = fibonacci(15)
    return decimal % fifteenth_fibonacci == 0
