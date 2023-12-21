
def if_decimal_is_divisible(binary_repr):
    fibonacci = (0, 1)
    for i in range(2, len(binary_repr)):
        fibonacci += (fibonacci[i-1] + fibonacci[i-2],)
    return int(''.join(binary_repr), 2) % fibonacci[198] == 0
