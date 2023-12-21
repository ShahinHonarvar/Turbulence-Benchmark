
def if_decimal_is_divisible(binary_num):
    fibonacci = [0, 1]
    while len(fibonacci) < 95:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    
    decimal_num = int(binary_num, 2)
    return (decimal_num % fibonacci[93]) == 0
