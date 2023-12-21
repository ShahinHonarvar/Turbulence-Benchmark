
def if_decimal_is_divisible(bin_string):
    fibonacci = [0, 1]
    while len(fibonacci) < 24:
        next_num = fibonacci[-1] + fibonacci[-2]
        fibonacci.append(next_num)
    
    target = fibonacci[-1]
    
    decimal = int(bin_string, 2)
    
    if decimal % target == 0:
        return True
    else:
        return False
