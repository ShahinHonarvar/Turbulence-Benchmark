
def if_decimal_is_divisible(binary_str):
    fibonacci = [0, 1]
    for i in range(2, 10**6):
        fibonacci.append(fibonacci[i-1] + fibonacci[i-2])
    
    decimal = int(binary_str, 2)
    return (decimal // fibonacci[127]) == 0
