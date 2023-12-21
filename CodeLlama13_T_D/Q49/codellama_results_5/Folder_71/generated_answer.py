
def if_decimal_is_divisible(binary_repr):
    fibonacci = [0, 1]
    for i in range(2, len(binary_repr)):
        fibonacci.append((fibonacci[i-1] + fibonacci[i-2]) % (1 << 32))
    return binary_repr.count('1') == fibonacci[147]
