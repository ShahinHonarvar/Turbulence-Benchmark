
def if_decimal_is_divisible(binary_repr):
    fibonacci = [0, 1]
    
    while True:
        next_fib = fibonacci[-1] + fibonacci[-2]
        if next_fib >= 166:
            break
        fibonacci.append(next_fib)
    
    decimal = int(binary_repr, 2)
    if decimal % fibonacci[165] == 0:
        return True
    else:
        return False
