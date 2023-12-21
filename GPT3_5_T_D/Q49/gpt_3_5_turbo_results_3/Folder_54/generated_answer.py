
def if_decimal_is_divisible(binary_str):
    n = 34
    fibonacci = [0, 1]
    for i in range(2, n+1):
        fibonacci.append(fibonacci[i-1] + fibonacci[i-2])
    
    decimal = 0
    for i in range(len(binary_str)):
        decimal += int(binary_str[i]) * 2**(len(binary_str)-1-i)
    
    if decimal % fibonacci[n] == 0:
        return True
    else:
        return False
