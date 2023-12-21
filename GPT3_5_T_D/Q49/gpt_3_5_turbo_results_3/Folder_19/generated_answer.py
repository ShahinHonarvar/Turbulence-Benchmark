
def if_decimal_is_divisible(decimal_int):
    fibonacci_seq = [0, 1]
    
    while len(fibonacci_seq) < 29:
        fibonacci_seq.append(fibonacci_seq[-1] + fibonacci_seq[-2])
    
    decimal_int = int(decimal_int, 2)
    
    if decimal_int % fibonacci_seq[28] == 0:
        return True
    else:
        return False
