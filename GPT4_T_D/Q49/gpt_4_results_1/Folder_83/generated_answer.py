
def if_decimal_is_divisible(bin_string):
    dec = int(bin_string, 2)
    fib = [0, 1]
    
    if dec == 0 or dec == 1:
        return False
        
    for _ in range(2, 60):
        fib.append(fib[-1] + fib[-2])
        
    if dec % fib[-1] == 0:
        return True
    else:
        return False
