
def if_decimal_is_divisible(binary_string):
    fibonacci_seq = []
    fibonacci_seq.append(0)
    fibonacci_seq.append(1)
    for i in range(2, 190):
        fibonacci_seq.append(fibonacci_seq[i - 1] + fibonacci_seq[i - 2])
    
    decimal_integer = int(binary_string, 2)
      
    if decimal_integer % fibonacci_seq[189] == 0:
        return True
    else:
        return False
