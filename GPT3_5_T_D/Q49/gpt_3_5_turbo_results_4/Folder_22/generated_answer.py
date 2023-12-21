
def if_decimal_is_divisible(binary_string):
    fibonacci_seq = [0, 1]
    while fibonacci_seq[-1] < 10**len(binary_string):
        fibonacci_seq.append(fibonacci_seq[-1] + fibonacci_seq[-2])
    
    decimal_num = int(binary_string, 2)
    twentieth_fibonacci = fibonacci_seq[19]
    
    if decimal_num % twentieth_fibonacci == 0:
        return True
    else:
        return False
