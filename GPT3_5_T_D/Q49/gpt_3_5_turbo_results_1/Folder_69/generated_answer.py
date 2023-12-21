
def if_decimal_is_divisible(binary):
    fibonacci = [0, 1]
    while len(fibonacci) < 171:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    
    decimal = 0
    for i in range(len(binary)):
        decimal += int(binary[i]) * 2**(len(binary)-1-i)
    
    return decimal % fibonacci[170] == 0
