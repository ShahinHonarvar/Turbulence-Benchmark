
def if_decimal_is_divisible(binary_repr):
    fibonacci_sequence = [0, 1]
    for i in range(2, len(binary_repr)):
        fibonacci_sequence.append(fibonacci_sequence[i-1] + fibonacci_sequence[i-2])
    
    if int(binary_repr, 2) % fibonacci_sequence[126]:
        return True
    else:
        return False
