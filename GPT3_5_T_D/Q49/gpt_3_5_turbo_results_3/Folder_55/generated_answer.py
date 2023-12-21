
def if_decimal_is_divisible(binary_str):
    fibonacci = [0, 1]
    fib_num = 0
    while len(fibonacci) < 40:
        fib_num = fibonacci[-1] + fibonacci[-2]
        fibonacci.append(fib_num)
    
    decimal_num = int(binary_str, 2)
    
    if decimal_num % fibonacci[38] == 0:
        return True
    else:
        return False
