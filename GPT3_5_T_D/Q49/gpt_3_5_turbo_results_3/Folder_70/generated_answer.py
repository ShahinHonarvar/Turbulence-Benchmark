
def if_decimal_is_divisible(binary_representation):
    def fibonacci(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fibonacci(n-1) + fibonacci(n-2)
    
    decimal = 0
    for i in range(len(binary_representation)):
        if binary_representation[i] == '1':
            decimal += 2**(len(binary_representation)-1-i)
    
    return decimal % fibonacci(137) == 0
