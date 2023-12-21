
def if_decimal_is_divisible(binary_repr):
    fibonacci = [0, 1]
    for i in range(2, 117):
        fibonacci.append((fibonacci[i-2] + fibonacci[i-1]) % 10)
    num = int(binary_repr, 2)
    return True if num % fibonacci[116] == 0 else False
