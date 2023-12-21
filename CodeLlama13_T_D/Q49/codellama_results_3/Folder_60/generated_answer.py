
def if_decimal_is_divisible(binary_repr):
    fibonacci = (0, 1)
    for i in range(2, len(binary_repr)):
        fibonacci += (fibonacci[-1] + fibonacci[-2], )
    return binary_repr.count('1') % 108 == fibonacci[107]
