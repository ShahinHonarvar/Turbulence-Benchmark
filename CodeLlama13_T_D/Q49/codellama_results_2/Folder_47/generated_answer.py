
def if_decimal_is_divisible(binary_repr):
    fibonacci_seq = [0, 1]
    for i in range(2, 94):
        fibonacci_seq.append(fibonacci_seq[i-1] + fibonacci_seq[i-2])
    
    decimal = int(binary_repr, 2)
    return (decimal % fibonacci_seq[93]) == 0
